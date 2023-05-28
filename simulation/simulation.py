import pandas as pd
import numpy as np

def model_percent(check_sum, num_simulation, type_of_button_prob, type_of_percent_prob, buttons_set, ds_0):
    all_stats = []  # для сохранения результатов симуляции

    for i in range(num_simulation):
        # Выбираем случайно были ли чаевые оставлены вручную или была выбрана кнопка
        select_type_of_button = np.random.choice([0, 1], len(check_sum), p = type_of_button_prob)

        # Выбираем случайно сумму, которая была оставлена
        tips_amount = []
        select_button = []
        # if i % 1000 == 0:
        #     print(i)
        for j in range(len(check_sum)):
            if select_type_of_button[j] == 0:
                tips_amount.append(np.random.choice(ds_0, size = 1))
                select_button.append(tips_amount[j])
            else:
                select_button.append(np.random.choice(buttons_set, size=1, p=type_of_percent_prob))
                tips_amount.append(select_button[j] * check_sum[j] / 100)

        # Создание фрейма данных на основе входных значений и количества повторений
        dfr = pd.DataFrame(index=range(len(check_sum)), data={'amount': tips_amount,
                                                               'check_sum': check_sum,
                                                               'select_type_of_button': select_type_of_button,
                                                               'selected_button': select_button})
        # Определим средний процент чаевых
        average_tips = (dfr['amount'] / dfr['check_sum']).mean()

        # Мы хотим отслеживать общую сумму чаевых и средний размер чаевых по всем симуляциям
        all_stats.append(average_tips)

    return all_stats

def model_sum(check_sum, num_simulation, type_of_button_prob, type_of_percent_prob, buttons_set, ds_0):
    all_stats = []  # для сохранения результатов симуляции

    for i in range(num_simulation):
        # Выбираем случайно были ли чаевые оставлены вручную или была выбрана кнопка
        select_type_of_button = np.random.choice([0, 1], len(check_sum), p = type_of_button_prob)

        # Выбираем случайно сумму, которая была оставлена
        tips_amount = []

        # if i % 1000 == 0:
        #     print(i)
        for j in range(len(check_sum)):
            if select_type_of_button[j] == 0:
                tips_amount.append(np.random.choice(ds_0, size = 1))

            else:
                tips_amount.append(np.random.choice(buttons_set, size=1, p = type_of_percent_prob))

        # Создание фрейма данных на основе входных значений и количества повторений
        dfr = pd.DataFrame(index=range(len(check_sum)), data={'amount': tips_amount,
                                                               'check_sum': check_sum,
                                                               'select_type_of_button': select_type_of_button})
        dfr['p'] = dfr['amount'] / dfr['check_sum']
        # Определим средний процент чаевых
        average_tips = (dfr['amount'] / dfr['check_sum']).mean()
        # Мы хотим отслеживать средний размер чаевых по всем симуляциям
        all_stats.append(average_tips)

    return all_stats

