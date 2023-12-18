"""
------------------------------------------------------------------------------------------------------------------
                                            Семинар 9. Задача 42. Домашнее задание
Дан файл california_housing_train.csv.
Найти максимальное значение переменной "households" в зоне минимального значения переменной "population" 
и сохраните это значение в переменную max_households_in_min_population. Используйте модуль pandas.
""" 
# Подключаемые библиотеки
from pandas import read_csv

# Загрузка данных из файла california_housing_train.csv
data = read_csv("california_housing_train.csv")

# Фильтрация данных зона минимального значения переменной "population" 
filtered_data = data[data["population"] == data["population"].min()]

# Максимальное значение переменной "households" 
max_households_in_min_population = filtered_data["households"].max()
print(max_households_in_min_population)