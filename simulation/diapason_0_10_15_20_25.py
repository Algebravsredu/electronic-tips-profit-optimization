import pandas as pd
import numpy as np
import simulation as sim
import data_preparation as dp
import random
import time

df = pd.read_csv('/Users/Egor/Downloads/diapason_0.csv')

df = dp.data_prep(df, '[10, 15, 20, 25]')

print(df)

# res_prob = dp.probabilities(df, [10, 15, 20, 25], 0, 1000)
#
# print(df[df['type_of_selected_button'] == 1 ])

#создание массива сумм чека с исходным распределением
# check_sum = []
# check_sum_type = np.random.choice(range(66), 8000, p = res_prob[2])
#
# for i in range(8000):
#     for j in range(66):
#         if check_sum[i] == j:
#             check_sum.append(random.randrange(6600 + j * 50, 6600 + (j+1) * 50, 1))
#
# df_0 = df[df['type_of_selected_button'] == 0]['amount']
#
# start = time.time()
#
# stats = sim.model_percent(check_sum, 10000, res_prob[0], res_prob[1], [10,15,20,25], df, df_0)
#
# end = time.time() - start
#
# print(end)
#
# st = pd.DataFrame(stats)
#
# print(st)
#
# st.to_csv('/Users/Egor/Desktop/все/Результаты симуляций/diapason_7_10_15_20_25')