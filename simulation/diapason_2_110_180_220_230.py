import pandas as pd
import numpy as np
import simulation as sim
import data_preparation as dp
import random
import time

df = pd.read_csv('/Users/Egor/Downloads/diapason_2.csv')

df_p = dp.data_prep(df, '[110, 180, 220, 230]')

print(df_p)
res_prob = dp.probabilities(df_p, df, [110, 180, 220, 230], 1500, 2100)

# создание массива сумм чека с исходным распределением
check_sum = []
check_sum_type = np.random.choice(range(12), 6000, p = res_prob[2])

for i in range(6000):
    for j in range(12):
        if check_sum_type[i] == j:
            check_sum.append(random.randrange(1500 + j * 50, 1500 + (j+1) * 50, 1))

df_0 = df_p[df_p['type_of_selected_button'] == 0]['amount']

start = time.time()

stats = sim.model_sum(check_sum, 10000, res_prob[0], res_prob[1], [110,180,220,230],df_0)

end = time.time() - start

print(end)

st = pd.DataFrame(stats)

print(st)

st.to_csv('/Users/Egor/Desktop/все/Результаты симуляций/diapason_2_110_180_220_230')