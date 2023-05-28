import pandas as pd
import numpy as np
import simulation as sim
import data_preparation as dp
import random
import time

df = pd.read_csv('/Users/Egor/Downloads/diapason_7.csv')

df_p = dp.data_prep(df, '[250, 400, 450, 500]')

res_prob = dp.probabilities(df_p, df,  [250, 400, 450, 500], 5100, 6600)

#создание массива сумм чека с исходным распределением
check_sum = []
check_sum_type = np.random.choice([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29], 15000, p = res_prob[2])

for i in range(15000):
  if check_sum_type[i] == 0:
    check_sum.append(random.randrange(5100, 5150, 1))
  elif check_sum_type[i] == 1:
    check_sum.append(random.randrange(5150, 5200, 1))
  elif check_sum_type[i] == 2:
    check_sum.append(random.randrange(5200, 5250, 1))
  elif check_sum_type[i] == 3:
    check_sum.append(random.randrange(5250, 5300, 1))
  elif check_sum_type[i] == 4:
    check_sum.append(random.randrange(5300, 5350, 1))
  elif check_sum_type[i] == 5:
    check_sum.append(random.randrange(5350, 5400, 1))
  elif check_sum_type[i] == 6:
    check_sum.append(random.randrange(5400, 5450, 1))
  elif check_sum_type[i] == 7:
    check_sum.append(random.randrange(5450, 5500, 1))
  elif check_sum_type[i] == 8:
    check_sum.append(random.randrange(5500, 5550, 1))
  elif check_sum_type[i] == 9:
    check_sum.append(random.randrange(5550, 5600, 1))
  elif check_sum_type[i] == 10:
    check_sum.append(random.randrange(5600, 5650, 1))
  elif check_sum_type[i] == 11:
    check_sum.append(random.randrange(5650, 5700, 1))
  elif check_sum_type[i] == 12:
    check_sum.append(random.randrange(5700, 5750, 1))
  elif check_sum_type[i] == 13:
    check_sum.append(random.randrange(5750, 5800, 1))
  elif check_sum_type[i] == 14:
    check_sum.append(random.randrange(5800, 5850, 1))
  elif check_sum_type[i] == 15:
    check_sum.append(random.randrange(5850, 5900, 1))
  elif check_sum_type[i] == 16:
    check_sum.append(random.randrange(5900, 5950, 1))
  elif check_sum_type[i] == 17:
    check_sum.append(random.randrange(5950, 6000, 1))
  elif check_sum_type[i] == 18:
    check_sum.append(random.randrange(6000, 6050, 1))
  elif check_sum_type[i] == 19:
    check_sum.append(random.randrange(6050, 6100, 1))
  elif check_sum_type[i] == 20:
    check_sum.append(random.randrange(6100, 6150, 1))
  elif check_sum_type[i] == 21:
    check_sum.append(random.randrange(6150, 6200, 1))
  elif check_sum_type[i] == 22:
    check_sum.append(random.randrange(6200, 6250, 1))
  elif check_sum_type[i] == 23:
    check_sum.append(random.randrange(6250, 6300, 1))
  elif check_sum_type[i] == 24:
    check_sum.append(random.randrange(6300, 6350, 1))
  elif check_sum_type[i] == 25:
    check_sum.append(random.randrange(6350, 6400, 1))
  elif check_sum_type[i] == 26:
    check_sum.append(random.randrange(6400, 6450, 1))
  elif check_sum_type[i] == 27:
    check_sum.append(random.randrange(6450, 6500, 1))
  elif check_sum_type[i] == 28:
    check_sum.append(random.randrange(6500, 6550, 1))
  elif check_sum_type[i] == 29:
    check_sum.append(random.randrange(6550, 6600, 1))

df_0 = df_p[df_p['type_of_selected_button'] == 0]['amount']

start = time.time()

stats = sim.model_sum(check_sum, 10000, res_prob[0], res_prob[1], [250, 400, 450, 500], df_0)

end = time.time() - start

print(end)

st = pd.DataFrame(stats)

print(st)

st.to_csv('/Users/Egor/Desktop/все/Результаты симуляций/diapason_7_250_400_450_500')