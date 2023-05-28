import pandas as pd
import numpy as np

#Подготовка данных для моделей с конкретными суммами и с процентами
def data_prep(dataframe, set_of_buttons):
    dataframe = dataframe[dataframe['amount'] > 0] #убираем данные, где значение чаевых <0
    q = np.quantile(dataframe[dataframe['type_of_selected_button'] == 0]['amount'], 0.999) #определяем выбросы в случае, когда чаевые оставлены вручную
    dataframe = dataframe[dataframe['values'] == set_of_buttons].copy() #выбираем данные с рассматриваемым набором кнопок
    dataframe = dataframe[((dataframe['type_of_selected_button'] == 0) & (dataframe['amount'] <= q)) | (dataframe['type_of_selected_button'] != 0)] #удаляем выбросы
    return dataframe

#Подсчет вероятностей для дальнейшей симуляции
def probabilities(dataframe_1, dataframe_2, set_of_buttons, left, right):
    type_of_button_prob = [len(dataframe_1[dataframe_1['type_of_selected_button'] == 0]) / len(dataframe_1), # вероятности выбора ручного ввода и одной из кнопок
                        1 - len(dataframe_1[dataframe_1['type_of_selected_button'] == 0]) / len(dataframe_1)]

    #Вероятности выбора каждой из кнопок
    type_of_percent_prob = []
    for i in range(4):
        type_of_percent_prob.append(len(dataframe_1[(dataframe_1['type_of_selected_button'] != 0) & (dataframe_1['selected_button'] == set_of_buttons[i])])/
                                    len(dataframe_1[dataframe_1['type_of_selected_button'] != 0]))

    #Вероятность суммы чека на каждом интервале по 50 рублей
    interval = right - left
    h = interval // 50
    count = []
    for i in range(h):
        count.append(len(dataframe_2[(dataframe_2['check_sum'] > left + i * 50) & (dataframe_2['check_sum'] <= left + (i + 1) * 50)]) / len(dataframe_2))

    return (type_of_button_prob, type_of_percent_prob, count)

#Подготовка данных для моделирования в случае, когда наборы кнопок предлагаются случайно
def data_preparation_2(dataframe):
  dataframe = dataframe.drop('index', axis=1)
  dataframe = dataframe[dataframe['amount'] > 0].copy()
  q = np.quantile(dataframe[dataframe['type_of_selected_button'] == 0]['amount'], 0.999)
  dataframe = dataframe[((dataframe['type_of_selected_button'] == 0) & (dataframe['amount'] <= q)) | (
              dataframe['type_of_selected_button'] != 0)].copy()

  dataframe = dataframe.reset_index()

  number_of_selected_button = []
  for i in range(len(dataframe)):
      if dataframe['selected_button'][i] == dataframe['b_1'][i]:
          number_of_selected_button.append('b_1')
      elif dataframe['selected_button'][i] == dataframe['b_2'][i]:
          number_of_selected_button.append('b_2')
      elif dataframe['selected_button'][i] == dataframe['b_3'][i]:
          number_of_selected_button.append('b_3')
      elif dataframe['selected_button'][i] == dataframe['b_4'][i]:
          number_of_selected_button.append('b_4')
      else:
          number_of_selected_button.append(0)

  dataframe['number_of_selected_button'] = number_of_selected_button

  set_of_pop_comb = dataframe['values'].value_counts().index[:5] #Выбор 5 наиболее часто встречающихся комбинаций
  df_r = dataframe.copy()
  for i in range(5): #Отсавшиеся данные без 5 наиболее часто встречающихся комбинаций
    df_r = df_r[df_r['values'] != set_of_pop_comb[i]].copy()

  df_r = df_r.reset_index()

  set_of_comb = dataframe['values'].value_counts()

  set_of_comb_int = []

  for i in range(len(dataframe)): #Создание массива типа int для всех предлагаемых наборов кнопок для всех транзакций
      set_of_comb_int.append([dataframe['b_1'][i],
                              dataframe['b_2'][i],
                              dataframe['b_3'][i],
                              dataframe['b_4'][i]])
  dataframe['values_int'] = set_of_comb_int

  return(dataframe, df_r, set_of_comb)


#Подсчет вероятностей в случае моделирования со случайным предложением кнопок. Для 5 самых популярных наборов вероятности считаются индивидуально,
# для остальных наборов вероятности одинаковые
def probabilities_random(dataframe1, dataframe2, set_of_pop_comb, set_of_comb, left, right):
    # Вероятности предложения каждой транзакции из 5 самых популярных
    probability_of_combination = []
    sum = 0
    for i in range(5):
        probability_of_combination.append(
            len(dataframe1[dataframe1['values'] == set_of_pop_comb[i]]) / len(dataframe1))
        sum+= probability_of_combination[i]

    #если предлагалось больше 5 наборов всего, находим вероятности появления каждой комбинации
    if not dataframe2.empty:
        for i in range(len(set_of_comb) - 5):
            probability_of_combination.append((1 - sum) / (len(set_of_comb) - 5))

    probability_of_selecting_button = []

    for i in range(5):
        probability_of_selecting_button.append([len(dataframe1[
                                                       (dataframe1['values'] == set_of_pop_comb[i]) & (
                                                                   dataframe1['type_of_selected_button'] != 0)]) / len(
            dataframe1[dataframe1['values'] == set_of_pop_comb[i]]),
                                               1 - len(dataframe1[
                                                       (dataframe1['values'] == set_of_pop_comb[i]) & (
                                                                   dataframe1['type_of_selected_button'] != 0)]) / len(
            dataframe1[dataframe1['values'] == set_of_pop_comb[i]])])

    if not dataframe2.empty:
        p = len(dataframe2[dataframe2['type_of_selected_button'] != 0]) / len(dataframe2)
        for i in range(len(set_of_comb) - 5):
            probability_of_selecting_button.append([p, 1 - p])

    probability_of_every_button = []
    for i in range(5):
        probability_of_every_button.append([len(dataframe1[(dataframe1['values'] == set_of_pop_comb[i]) & (dataframe1['number_of_selected_button'] == 'b_1') & (dataframe1['type_of_selected_button'] != 0)]) / len(dataframe1[(dataframe1['values'] == set_of_pop_comb[i]) & (dataframe1['type_of_selected_button'] != 0)]),
                                            len(dataframe1[(dataframe1['values'] == set_of_pop_comb[i]) & (
                                                        dataframe1['number_of_selected_button'] == 'b_2') & (dataframe1['type_of_selected_button'] != 0)]) / len(
                                                dataframe1[(dataframe1['values'] == set_of_pop_comb[i]) & (
                                                            dataframe1['type_of_selected_button'] != 0)]),
                                            len(dataframe1[(dataframe1['values'] == set_of_pop_comb[i]) & (
                                                        dataframe1['number_of_selected_button'] == 'b_3') & (dataframe1['type_of_selected_button'] != 0)]) / len(
                                                dataframe1[(dataframe1['values'] == set_of_pop_comb[i]) & (
                                                            dataframe1['type_of_selected_button'] != 0)]),
                                            len(dataframe1[(dataframe1['values'] == set_of_pop_comb[i]) & (
                                                        dataframe1['number_of_selected_button'] == 'b_4')& (dataframe1['type_of_selected_button'] != 0)]) / len(
                                                dataframe1[(dataframe1['values'] == set_of_pop_comb[i]) & (dataframe1['type_of_selected_button'] != 0)])])

    if not dataframe2.empty:
        a = len(dataframe2[(dataframe2['number_of_selected_button'] == 'b_1') & (dataframe2['type_of_selected_button'] != 0)]) / len(
            dataframe2[dataframe2['type_of_selected_button'] != 0])
        b = len(dataframe2[(dataframe2['number_of_selected_button'] == 'b_2') & (dataframe2['type_of_selected_button'] != 0)]) / len(
                 dataframe2[dataframe2['type_of_selected_button'] != 0])
        c = len(dataframe2[(dataframe2['number_of_selected_button'] == 'b_3') & (dataframe2['type_of_selected_button'] != 0)]) / len(
                 dataframe2[dataframe2['type_of_selected_button'] != 0])
        p = [a, b, c, 1 - (a+b+c)]
        for i in range(len(set_of_comb) - 5):
            probability_of_every_button.append(p)

    probability_of_every_button = pd.Series(data = probability_of_every_button, index = set_of_comb)

    # Вероятность суммы чека на каждом интервале по 50 рублей
    interval = right - left
    h = interval // 50
    count = []
    for i in range(h):
        count.append(len(dataframe1[(dataframe1['check_sum'] > left + i * 50) & (
                    dataframe1['check_sum'] <= left + (i + 1) * 50)]) / len(dataframe1))


    return probability_of_combination, probability_of_selecting_button, probability_of_every_button, count