import pandas as pd
import numpy as np
import simulation as sim
import data_preparation as dp
import random
import time

df = pd.read_csv('/Users/Egor/Downloads/diapason_2.csv')

df_p = dp.data_prep(df, '[10, 13, 17, 21]')

res_prob = dp.probabilities(df_p, df, [10, 13, 17, 21], 1500, 2100)

# создание массива сумм чека с исходным распределением
check_sum = []
check_sum_type = np.random.choice([0,1,2,3,4,5,6,7,8,9, 10, 11], 6000, p = res_prob[2])

for i in range(6000):
  if check_sum_type[i] == 0:
    check_sum.append(random.randrange(1500, 1550, 1))
  elif check_sum_type[i] == 1:
    check_sum.append(random.randrange(1550, 1600, 1))
  elif check_sum_type[i] == 2:
    check_sum.append(random.randrange(1600, 1650, 1))
  elif check_sum_type[i] == 3:
    check_sum.append(random.randrange(1650, 1700, 1))
  elif check_sum_type[i] == 4:
    check_sum.append(random.randrange(1700, 1750, 1))
  elif check_sum_type[i] == 5:
    check_sum.append(random.randrange(1750, 1800, 1))
  elif check_sum_type[i] == 6:
    check_sum.append(random.randrange(1800, 1850, 1))
  elif check_sum_type[i] == 7:
    check_sum.append(random.randrange(1850, 1900, 1))
  elif check_sum_type[i] == 8:
    check_sum.append(random.randrange(1900, 1950, 1))
  elif check_sum_type[i] == 9:
    check_sum.append(random.randrange(1950, 2000, 1))
  elif check_sum_type[i] == 10:
    check_sum.append(random.randrange(2000, 2050, 1))
  elif check_sum_type[i] == 11:
    check_sum.append(random.randrange(2050, 2100, 1))

df_0 = df_p[df_p['type_of_selected_button'] == 0]['amount']

start = time.time()

stats = sim.model_percent(check_sum, 10000, res_prob[0], res_prob[1], [10,13,17,21], df_0)

end = time.time() - start

print(end)

st = pd.DataFrame(stats)

print(st)

st.to_csv('/Users/Egor/Desktop/все/Результаты симуляций/diapason_2_10_13_17_21')