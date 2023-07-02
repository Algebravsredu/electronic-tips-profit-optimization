import pandas as pd
import numpy as np

def model_random(check_sum, num_simulation, type_of_comb_prob, type_of_but_prob, every_but_prob,  set_of_combinations, set_of_comb_with_type,ds_0, s_o_c, p_1):
    #подается на вход смоделированный набор сумм чека, число симуляций, вероятности предложения наборов, вероятности выбора набора или ручного ввода, вероятности выбора каждой кнопки из 4, наборы предлагаемых кнопок, наборы кнопок с типом, набор чаевых ручного ввода, 
    ,,
    all_stats = []  # для сохранения результатов симуляции

    for i in range(num_simulation):
        # Выбираем случайно, какой набор был предложен
        select_type_of_combination = np.random.choice(set_of_combinations.index, len(check_sum), p = type_of_comb_prob)

        # Выбираем случайно был ли выбран ручной ввод или была нажата кнопка
        type_of_selected_button = []
        for j in range(len(check_sum)):
            if select_type_of_combination[j] == set_of_combinations.index[0]:
                type_of_selected_button.append(np.random.choice([1,0], 1, p = type_of_but_prob[0]))
            elif select_type_of_combination[j] == set_of_combinations.index[1]:
                type_of_selected_button.append(np.random.choice([1,0], 1, p = type_of_but_prob[1]))
            elif select_type_of_combination[j] == set_of_combinations.index[2]:
                type_of_selected_button.append(np.random.choice([1,0], 1, p = type_of_but_prob[2]))
            elif select_type_of_combination[j] == set_of_combinations.index[3]:
                type_of_selected_button.append(np.random.choice([1,0], 1, p = type_of_but_prob[3]))
            elif select_type_of_combination[j] == set_of_combinations.index[4]:
                type_of_selected_button.append(np.random.choice([1, 0], 1, p = type_of_but_prob[4]))
            else:
                type_of_selected_button.append(np.random.choice([1, 0], 1, p = type_of_but_prob[5]))

        #Если была нажата кнопка, случайно выбираем, какая из четырех была нажата
        tips_amount = []
        select_button = []

        for j in range(len(check_sum)):
            if type_of_selected_button[j] == 0:
                tips_amount.append(np.random.choice(ds_0, size=1))
                select_button.append(tips_amount[j])
            else:
                if select_type_of_combination[j] == set_of_combinations.index[0]:
                    if set_of_comb_with_type[select_type_of_combination[j]] == 2:
                        select_button.append(np.random.choice(s_o_c[0], size=1, p=p_1))
                        tips_amount.append(select_button[j])
                    else:
                        select_button.append(np.random.choice(s_o_c[0], size=1, p=p_1))
                        tips_amount.append(select_button[j] * check_sum[j] / 100)
                else:
                    if set_of_comb_with_type[select_type_of_combination[j]] == 2:
                        select_button.append(np.random.choice(set_of_combinations[select_type_of_combination[j]], size=1, p=every_but_prob[select_type_of_combination[j]]))
                        tips_amount.append(select_button[j])
                    else:
                        select_button.append(np.random.choice(set_of_combinations[select_type_of_combination[j]], size=1, p=every_but_prob[select_type_of_combination[j]]))
                        tips_amount.append(select_button[j] * check_sum[j] / 100)


        # Создание фрейма данных на основе входных значений и количества повторений
        dfr = pd.DataFrame(index=range(len(check_sum)), data={'amount': tips_amount,
                                                               'check_sum': check_sum,
                                                              'select_type_of_comb': select_type_of_combination,
                                                               'select_type_of_button': type_of_selected_button,
                                                               'selected_button': select_button})

        # Определим средний процент чаевых
        average_tips = (dfr['amount'] / dfr['check_sum']).mean()

        # Мы хотим отслеживать средний размер чаевых по всем симуляциям
        all_stats.append(average_tips)

    return all_stats
