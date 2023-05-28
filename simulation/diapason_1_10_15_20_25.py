import pandas as pd
import numpy as np
import simulation as sim
import data_preparation as dp
import random
import time

df = pd.read_csv('/Users/Egor/Downloads/diapason_1.csv')

df_p = dp.data_prep(df, '[10, 15, 20, 25]')

res_prob = dp.probabilities(df_p, df, [10, 15, 20, 25], 1000, 1500)

# создание массива сумм чека с исходным распределением
check_sum = []
check_sum_type = np.random.choice([0,1,2,3,4,5,6,7,8,9], 5000, p = res_prob[2])

for i in range(5000):
  if check_sum_type[i] == 0:
    check_sum.append(random.randrange(1000, 1050, 1))
  elif check_sum_type[i] == 1:
    check_sum.append(random.randrange(1050, 1100, 1))
  elif check_sum_type[i] == 2:
    check_sum.append(random.randrange(1100, 1150, 1))
  elif check_sum_type[i] == 3:
    check_sum.append(random.randrange(1150, 1200, 1))
  elif check_sum_type[i] == 4:
    check_sum.append(random.randrange(1200, 1250, 1))
  elif check_sum_type[i] == 5:
    check_sum.append(random.randrange(1250, 1300, 1))
  elif check_sum_type[i] == 6:
    check_sum.append(random.randrange(1300, 1350, 1))
  elif check_sum_type[i] == 7:
    check_sum.append(random.randrange(1350, 1400, 1))
  elif check_sum_type[i] == 8:
    check_sum.append(random.randrange(1400, 1450, 1))
  elif check_sum_type[i] == 9:
    check_sum.append(random.randrange(1450, 1500, 1))

df_0 = df_p[df_p['type_of_selected_button'] == 0]['amount']

start = time.time()

stats = sim.model_percent(check_sum, 10000, res_prob[0], res_prob[1], [10,15,20,25],df_0)

end = time.time() - start

print(end)

st = pd.DataFrame(stats)

print(st)

st.to_csv('/Users/Egor/Desktop/все/Результаты симуляций/diapason_1_10_15_20_25')