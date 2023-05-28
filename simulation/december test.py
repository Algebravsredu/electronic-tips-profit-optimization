import csv
import pandas as pd

df = pd.read_csv("/Users/Egor/Downloads/Кнопки 0123.csv", delimiter="\\", encoding='utf-8')
print(df)

with open("/Users/Egor/Downloads/Кнопки 0123.csv", encoding='utf-8') as r_file:
    # Создаем объект DictReader, указываем символ-разделитель ","
    file_reader = csv.DictReader(r_file, delimiter = "\\")
    # Счетчик для подсчета количества строк и вывода заголовков столбцов
    count = 0
    # Считывание данных из CSV файла
    df = pd.read_csv(file_reader)
    print(df)