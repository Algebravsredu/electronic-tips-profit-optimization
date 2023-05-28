import pandas as pd
import numpy as np
import simulation as sim
import simulation_test as simt
import data_preparation as dp
import random
import time

df = pd.read_csv('/Users/Egor/Downloads/diapason_7.csv')

d = dp.data_preparation_2(df)

set = d[2]

set_int = d[0]['values_int'].value_counts()

set_of_comb = pd.Series(data = set_int.index, index = set.index)

type_of_offered_button = []
for comb in set_of_comb.values:
    if comb[3] >= 100:
        type_of_offered_button.append(2)
    else:
        type_of_offered_button.append(1)

set_of_comb_w_type = pd.Series(data = type_of_offered_button, index = set.index)

dd = d[0]

p = dp.probabilities_random(d[0], d[1], set.index[:5], set.index, 5100, 6600)

 # #создание массива сумм чека с исходным распределением
check_sum = []
check_sum_type = np.random.choice(range(30), 15000, p = p[3])

for i in range(15000):
    for j in range(30):
        if check_sum_type[i] == j:
            check_sum.append(random.randrange(5100 + j * 50, 5100 + (j+1) * 50, 1))

ds_0 = dd[dd['type_of_selected_button'] == 0]['amount']

start = time.time()
stats = simt.model_random(check_sum, 10000, p[0], p[1], p[2], set_of_comb, set_of_comb_w_type, ds_0, set_of_comb.values[:5], p[2].values[0])
end = time.time() - start
print(end)

st = pd.DataFrame(stats)

print(st)

st.to_csv('/Users/Egor/Desktop/все/Результаты симуляций/diapason_7_random')

