import pandas as pd
import numpy as np
import simulation as sim
import data_preparation as dp
import random
import time

df = pd.read_csv('/Users/Egor/Downloads/diapason_3.csv')

df_p = dp.data_prep(df, '[7, 10, 15, 20]')
res_prob = dp.probabilities(df_p, df, [7, 10, 15, 20], 2100, 2700)

print(res_prob)
# создание массива сумм чека с исходным распределением
check_sum = []
check_sum_type = np.random.choice([0,1,2,3,4,5,6,7,8,9,10,11], 6000, p = res_prob[2])

for i in range(6000):
  if check_sum_type[i] == 0:
    check_sum.append(random.randrange(2100, 2150, 1))
  elif check_sum_type[i] == 1:
    check_sum.append(random.randrange(2150, 2200, 1))
  elif check_sum_type[i] == 2:
    check_sum.append(random.randrange(2200, 2250, 1))
  elif check_sum_type[i] == 3:
    check_sum.append(random.randrange(2250, 2300, 1))
  elif check_sum_type[i] == 4:
    check_sum.append(random.randrange(2300, 2350, 1))
  elif check_sum_type[i] == 5:
    check_sum.append(random.randrange(2350, 2400, 1))
  elif check_sum_type[i] == 6:
    check_sum.append(random.randrange(2400, 2450, 1))
  elif check_sum_type[i] == 7:
    check_sum.append(random.randrange(2450, 2500, 1))
  elif check_sum_type[i] == 8:
    check_sum.append(random.randrange(2500, 2550, 1))
  elif check_sum_type[i] == 9:
    check_sum.append(random.randrange(2550, 2600, 1))
  elif check_sum_type[i] == 10:
    check_sum.append(random.randrange(2600, 2650, 1))
  elif check_sum_type[i] == 11:
    check_sum.append(random.randrange(2650, 2700, 1))

df_0 = df_p[df_p['type_of_selected_button'] == 0]['amount']

start = time.time()

stats = sim.model_percent(check_sum, 10000, res_prob[0], res_prob[1], [7,10,15,20], df_0)

end = time.time() - start

print(end)

st = pd.DataFrame(stats)

print(st)

st.to_csv('/Users/Egor/Desktop/все/Результаты симуляций/diapason_3_7_10_15_20')