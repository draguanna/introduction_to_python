"""
------------------------------------------------------------------------------------------------------------------
                                            Семинар 9. Задача 40. Домашнее задание
Дан файл california_housing_train.csv. Определить среднюю стоимость дома, где количество людей от 0 до 500 
(population) и сохранить ее в переменную avg. Используйте модуль pandas.
""" 
# Подключаемые библиотеки
from pandas import read_csv

# Загрузка данных из файла california_housing_train.csv
data = read_csv("california_housing_train.csv")

# Фильтрация данных по количеству людей от 0 до 500
filtered_data = data[(data['population'] >= 0) & (data['population'] <= 500)]

# Вычисление средней стоимости дома
avg = filtered_data['median_house_value'].mean()

print(avg)