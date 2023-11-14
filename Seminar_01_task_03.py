"""
------------------------------------------------------------------------------------------------------------------
                                            Семинар 1. Задача №3.
В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. 
За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов. 
Выведите наименьшее число парт, которое нужно приобрести для них.
------------------------------------------------------------------------------------------------------------------
"""
# Импорт модулей
from math import ceil

# Исходные параметры
n_1 = 20
n_2 = 21
n_3 = 22

# Вычисление результата
result = ceil(n_1/2) + ceil(n_2/2) + ceil(n_3/2)
print(f'Количество парт: {result}')
