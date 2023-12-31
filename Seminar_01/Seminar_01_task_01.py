"""
------------------------------------------------------------------------------------------------------------------
                                            Семинар 1. Задача №1.
За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров?
При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
------------------------------------------------------------------------------------------------------------------
"""
# Импорт модулей
from math import ceil

# Исходные параметры
n = 700
m = 750

# Вычисление результата
result = ceil(m / n)
print(f'Количество дней: {result}')