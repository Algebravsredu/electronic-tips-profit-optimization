import pandas as pd
import numpy as np
import simulation as sim
import data_preparation as dp
import random
import time

df = pd.read_csv('/Users/Egor/Downloads/diapason_5.csv')

df_p = dp.data_prep(df, '[180, 270, 320, 370]')

res_prob = dp.probabilities(df_p, df, [180, 270, 320, 370], 3300, 4100)
#создание массива сумм чека с исходным распределением
check_sum = []
check_sum_type = np.random.choice([0,1,2,3,4,5,6,7,8,9,10,11, 12, 13, 14, 15], 8000, p = res_prob[2])

for i in range(8000):
  if check_sum_type[i] == 0:
    check_sum.append(random.randrange(3300, 3350, 1))
  elif check_sum_type[i] == 1:
    check_sum.append(random.randrange(3350, 3400, 1))
  elif check_sum_type[i] == 2:
    check_sum.append(random.randrange(3400, 3450, 1))
  elif check_sum_type[i] == 3:
    check_sum.append(random.randrange(3450, 3500, 1))
  elif check_sum_type[i] == 4:
    check_sum.append(random.randrange(3500, 3550, 1))
  elif check_sum_type[i] == 5:
    check_sum.append(random.randrange(3550, 3600, 1))
  elif check_sum_type[i] == 6:
    check_sum.append(random.randrange(3600, 3650, 1))
  elif check_sum_type[i] == 7:
    check_sum.append(random.randrange(3650, 3700, 1))
  elif check_sum_type[i] == 8:
    check_sum.append(random.randrange(3700, 3750, 1))
  elif check_sum_type[i] == 9:
    check_sum.append(random.randrange(3750, 3800, 1))
  elif check_sum_type[i] == 10:
    check_sum.append(random.randrange(3800, 3850, 1))
  elif check_sum_type[i] == 11:
    check_sum.append(random.randrange(3850, 3900, 1))
  elif check_sum_type[i] == 12:
    check_sum.append(random.randrange(3900, 3950, 1))
  elif check_sum_type[i] == 13:
    check_sum.append(random.randrange(3950, 4000, 1))
  elif check_sum_type[i] == 14:
    check_sum.append(random.randrange(4000, 4050, 1))
  elif check_sum_type[i] == 15:
    check_sum.append(random.randrange(4050, 4100, 1))

df_0 = df_p[df_p['type_of_selected_button'] == 0]['amount']

start = time.time()

stats = sim.model_sum(check_sum, 10000, res_prob[0], res_prob[1], [180, 270, 320, 370], df_0)

end = time.time() - start

print(end)

st = pd.DataFrame(stats)

print(st)

st.to_csv('/Users/Egor/Desktop/все/Результаты симуляций/diapason_5_180_270_320_370')