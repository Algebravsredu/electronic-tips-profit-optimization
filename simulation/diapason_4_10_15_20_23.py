import pandas as pd
import numpy as np
import simulation as sim
import data_preparation as dp
import random
import time

df = pd.read_csv('/Users/Egor/Downloads/diapason_4.csv')

df_p = dp.data_prep(df, '[10, 15, 20, 23]')

res_prob = dp.probabilities(df_p, df, [10, 15, 20, 23], 2700, 3300)

#создание массива сумм чека с исходным распределением
check_sum = []
check_sum_type = np.random.choice([0,1,2,3,4,5,6,7,8,9,10,11], 6000, p = res_prob[2])

for i in range(6000):
  if check_sum_type[i] == 0:
    check_sum.append(random.randrange(2700, 2750, 1))
  elif check_sum_type[i] == 1:
    check_sum.append(random.randrange(2750, 2800, 1))
  elif check_sum_type[i] == 2:
    check_sum.append(random.randrange(2800, 2850, 1))
  elif check_sum_type[i] == 3:
    check_sum.append(random.randrange(2850, 2900, 1))
  elif check_sum_type[i] == 4:
    check_sum.append(random.randrange(2900, 2950, 1))
  elif check_sum_type[i] == 5:
    check_sum.append(random.randrange(2950, 3000, 1))
  elif check_sum_type[i] == 6:
    check_sum.append(random.randrange(3000, 3050, 1))
  elif check_sum_type[i] == 7:
    check_sum.append(random.randrange(3050, 3100, 1))
  elif check_sum_type[i] == 8:
    check_sum.append(random.randrange(3100, 3150, 1))
  elif check_sum_type[i] == 9:
    check_sum.append(random.randrange(3150, 3200, 1))
  elif check_sum_type[i] == 10:
    check_sum.append(random.randrange(3200, 3250, 1))
  elif check_sum_type[i] == 11:
    check_sum.append(random.randrange(3250, 3300, 1))

df_0 = df_p[df_p['type_of_selected_button'] == 0]['amount']

start = time.time()

stats = sim.model_percent(check_sum,  10000, res_prob[0], res_prob[1], [10,15,20,23], df_0)

end = time.time() - start

print(end)

st = pd.DataFrame(stats)

print(st)

st.to_csv('/Users/Egor/Desktop/все/Результаты симуляций/diapason_4_10_15_20_23')