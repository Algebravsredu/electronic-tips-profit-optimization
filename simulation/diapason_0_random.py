import pandas as pd
import numpy as np
import simulation as sim
import simulation_test as simt
import data_preparation as dp
import random
import time

df = pd.read_csv('/Users/Egor/Downloads/diapason_0.csv')

set = df['values'].value_counts()

d = dp.data_preparation_2(df)
dd = d[0]

p = dp.probabilities_random(d[0], d[1], set.index[:5], set.index, 0, 1000)


#создание массива сумм чека с исходным распределением
check_sum = []
check_sum_type = np.random.choice(range(20), 10000, p = p[3])

for i in range(10000):
    for j in range(20):
        if check_sum_type[i] == j:
            check_sum.append(random.randrange(j * 50, (j+1) * 50, 1))


ds_0 = dd[dd['type_of_selected_button'] == 0]['amount']

start = time.time()
stats = simt.model_random(check_sum, 10000, p[0], p[1], p[2], set.index, ds_0, dd, d[2], d[3])
end = time.time() - start

st = pd.DataFrame(stats)

print(end)

st.to_csv('/Users/Egor/Desktop/все/Результаты симуляций/diapason_0_random')

