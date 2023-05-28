import pandas as pd
import numpy as np
import simulation as sim
import simulation_test as simt
import limit_percent_simulation as tims
import data_preparation as dp
import random
import time

df = pd.read_csv('/Users/Egor/Downloads/d6.csv')
df = df[(df['region'] =='Москва') & (df['price_segment'] == 'Премиум (>2500)')]
df_random = df[(df['values'] != '[10, 13, 17, 22]')]
d_random = dp.data_preparation_2(df_random)

set = d_random[2]

set_int = d_random[0]['values_int'].value_counts()

set_of_comb = pd.Series(data = set_int.index, index = set.index)

df_exact = dp.data_prep(df, '[10, 13, 17, 22]')

type_of_offered_button = []
for comb in set_of_comb.values:
    if comb[3] >= 100:
        type_of_offered_button.append(2)
    else:
        type_of_offered_button.append(1)


set_of_comb_w_type = pd.Series(data = type_of_offered_button, index = set.index)

dd = d_random[0]

p = dp.probabilities_random(dd, d_random[1], set.index[:5], set.index, 4100, 5100)

res_prob = dp.probabilities(df_exact, df, [10, 13, 17, 22], 4100, 5100)

#создание массива сумм чека с исходным распределением
check_sum = []
check_sum_type = np.random.choice([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16, 17, 18, 19], 5000, p = res_prob[2])

for i in range(5000):
  if check_sum_type[i] == 0:
    check_sum.append(random.randrange(4100, 4150, 1))
  elif check_sum_type[i] == 1:
    check_sum.append(random.randrange(4150, 4200, 1))
  elif check_sum_type[i] == 2:
    check_sum.append(random.randrange(4200, 4250, 1))
  elif check_sum_type[i] == 3:
    check_sum.append(random.randrange(4250, 4300, 1))
  elif check_sum_type[i] == 4:
    check_sum.append(random.randrange(4300, 4350, 1))
  elif check_sum_type[i] == 5:
    check_sum.append(random.randrange(4350, 4400, 1))
  elif check_sum_type[i] == 6:
    check_sum.append(random.randrange(4400, 4450, 1))
  elif check_sum_type[i] == 7:
    check_sum.append(random.randrange(4450, 4500, 1))
  elif check_sum_type[i] == 8:
    check_sum.append(random.randrange(4500, 4550, 1))
  elif check_sum_type[i] == 9:
    check_sum.append(random.randrange(4550, 4600, 1))
  elif check_sum_type[i] == 10:
    check_sum.append(random.randrange(4600, 4650, 1))
  elif check_sum_type[i] == 11:
    check_sum.append(random.randrange(4650, 4700, 1))
  elif check_sum_type[i] == 12:
    check_sum.append(random.randrange(4700, 4750, 1))
  elif check_sum_type[i] == 13:
    check_sum.append(random.randrange(4750, 4800, 1))
  elif check_sum_type[i] == 14:
    check_sum.append(random.randrange(4800, 4850, 1))
  elif check_sum_type[i] == 15:
    check_sum.append(random.randrange(4850, 4900, 1))
  elif check_sum_type[i] == 16:
    check_sum.append(random.randrange(4900, 4950, 1))
  elif check_sum_type[i] == 17:
    check_sum.append(random.randrange(4950, 5000, 1))
  elif check_sum_type[i] == 18:
    check_sum.append(random.randrange(5000, 5050, 1))
  elif check_sum_type[i] == 19:
    check_sum.append(random.randrange(5050, 5100, 1))

ds_1 = dd[dd['type_of_selected_button'] == 0]['amount']
ds_0 = df_exact[df_exact['type_of_selected_button'] == 0]['amount']

start = time.time()
stats = tims.model_sim_perc(check_sum, 1, res_prob[0], res_prob[1], [10, 13, 17, 22], ds_0, p[0], p[1], p[2], set_of_comb, set_of_comb_w_type, set_of_comb.values[:5], p[2].values[0], ds_1)
end = time.time() - start
print(end)

st = pd.DataFrame(stats)

print(st.mean())
#
# #st.to_csv('/Users/Egor/Desktop/все/Результаты симуляций/diapason_6_random')
#
