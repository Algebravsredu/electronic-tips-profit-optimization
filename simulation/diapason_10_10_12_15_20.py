import pandas as pd
import numpy as np
import simulation as sim
import data_preparation as dp
import random
import time

df = pd.read_csv('/Users/Egor/Downloads/diapason_10.csv')

df = df[df['check_sum'] <= np.quantile(df['check_sum'], 0.99)]

df_p = dp.data_prep(df, '[10, 12, 15, 20]')

if df_p['check_sum'].max() % 50 == 0:
    right = int(df_p['check_sum'].max())
else:
    right = int(df_p['check_sum'].max() + 50 - df_p['check_sum'].max() % 50)

res_prob = dp.probabilities(df_p, df, [10, 12, 15, 20], 14900, right)

rp = res_prob[2][1:]
res_prob_2 = pd.Series(rp)
rp.append(1-res_prob_2.sum())

h = (right - 14900) // 50
#создание массива сумм чека с исходным распределением
check_sum = []
check_sum_type = np.random.choice(range(h), 10000, p = rp)
for i in range(10000):
    for j in range(h):
        if check_sum_type[i] == j:
            check_sum.append(random.randrange(14900 + j * 50, 14900 + (j+1) * 50, 1))

df_0 = df_p[df_p['type_of_selected_button'] == 0]['amount']

start = time.time()

stats = sim.model_percent(check_sum, 10000, res_prob[0], res_prob[1], [10,12,25,20], df_0)

end = time.time() - start

print(end)

st = pd.DataFrame(stats)

print(st)

st.to_csv('/Users/Egor/Desktop/все/Результаты симуляций/diapason_10_10_12_15_20')