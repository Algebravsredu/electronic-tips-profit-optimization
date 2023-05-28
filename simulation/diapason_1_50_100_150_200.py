import pandas as pd
import numpy as np
import simulation as sim
import data_preparation as dp
import random
import time

df = pd.read_csv('/Users/Egor/Downloads/diapason_1.csv')

df_p = dp.data_prep(df, '[50, 100, 150, 200]')

res_prob = dp.probabilities(df_p, df, [50, 100, 150, 200], 1000, 1500)

# создание массива сумм чека с исходным распределением
check_sum = []
check_sum_type = np.random.choice(range(10), 5000, p = res_prob[2])

for i in range(5000):
    for j in range(10):
        if check_sum_type[i] == j:
            check_sum.append(random.randrange(1000 + j * 50, 1000 + (j+1) * 50, 1))

df_0 = df_p[df_p['type_of_selected_button'] == 0]['amount']

start = time.time()

stats = sim.model_sum(check_sum, 10000, res_prob[0], res_prob[1], [50,100,150,200],df_0)

end = time.time() - start

print(end)

st = pd.DataFrame(stats)

print(st.mean())

st.to_csv('/Users/Egor/Desktop/все/Результаты симуляций/diapason_1_50_100_150_200')