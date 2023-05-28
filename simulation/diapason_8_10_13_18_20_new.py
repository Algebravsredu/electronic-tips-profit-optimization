import pandas as pd
import numpy as np
import simulation as sim
import data_preparation as dp
import random
import time

df = pd.read_csv('/Users/Egor/Downloads/diapason_8_new.csv')
df = df[df['values'] == '[10, 13, 18, 20]']
df_p = dp.data_prep(df, '[10, 13, 18, 20]')

res_prob = dp.probabilities(df_p, df,  [10, 13, 18, 20], 6600, 9000)

#создание массива сумм чека с исходным распределением
check_sum = []
check_sum_type = np.random.choice(range(48), 24000, p = res_prob[2])

for i in range(24000):
    for j in range(48):
        if check_sum_type[i] == j:
            check_sum.append(random.randrange(6600 + j * 50, 6600 + (j+1) * 50, 1))

df_0 = df_p[df_p['type_of_selected_button'] == 0]['amount']

start = time.time()

stats = sim.model_percent(check_sum, 10000, res_prob[0], res_prob[1], [10,13,18,20], df_0)

end = time.time() - start

print(end)

st = pd.DataFrame(stats)

print(st.mean())

st.to_csv('/Users/Egor/Desktop/все/Результаты симуляций/diapason_8_10_13_18_20_new')