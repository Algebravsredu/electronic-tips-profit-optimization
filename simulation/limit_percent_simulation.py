import pandas as pd
import numpy as np
import simulation_test as simt
import simulation as sim

def model_sim_perc(check_sum, num_simulation, type_of_button_prob_exact, type_of_percent_prob_exact, buttons_set_exact, ds_0,  type_of_comb_prob, type_of_but_prob, every_but_prob,  set_of_combinations, set_of_comb_with_type, s_o_c, p_1, ds_1):
    all_stats = []  # для сохранения результатов симуляции

    for i in range(num_simulation):
        if i%100 == 0:
            print(i)
        #Выбираем случайно был ли показан набор или случайно выбрали набор:
        select_set = np.random.choice([0, 1], p = [0, 1])
        if select_set == 0:
            r = pd.DataFrame(sim.model_percent(check_sum, 100, type_of_button_prob_exact, type_of_percent_prob_exact, buttons_set_exact, ds_0))
            all_stats.append(r.mean())
        else:
            r = pd.DataFrame(simt.model_random(check_sum, 1000, type_of_comb_prob, type_of_but_prob, every_but_prob,  set_of_combinations, set_of_comb_with_type,ds_1, s_o_c, p_1))
            all_stats.append(r.mean())

    return all_stats

def model_sim_sum(check_sum, num_simulation, type_of_button_prob_exact, type_of_percent_prob_exact, buttons_set_exact, ds_0,  type_of_comb_prob, type_of_but_prob, every_but_prob,  set_of_combinations, set_of_comb_with_type, s_o_c, p_1, ds_1):
    all_stats = []  # для сохранения результатов симуляции

    for i in range(num_simulation):
        if i % 100 == 0:
            print(i)
        #Выбираем случайно был ли показан набор или случайно выбрали набор:
        select_set = np.random.choice([0, 1], p = [0.95, 0.05])
        #(select_set)
        if select_set == 0:
            r = pd.DataFrame(sim.model_sum(check_sum, 100, type_of_button_prob_exact, type_of_percent_prob_exact, buttons_set_exact, ds_0))
            all_stats.append(r.mean())
        else:
            #print(select_set)
            r = pd.DataFrame(simt.model_random(check_sum, 1000, type_of_comb_prob, type_of_but_prob, every_but_prob,  set_of_combinations, set_of_comb_with_type,ds_1, s_o_c, p_1))
            all_stats.append(r.mean())

    return all_stats
