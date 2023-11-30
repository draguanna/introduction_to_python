"""
------------------------------------------------------------------------------------------------------------------
                                            Семинар 5. Задача 28. Домашнее задание
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
------------------------------------------------------------------------------------------------------------------
"""
# Введите ваше решение ниже

# Функция суммирования через рекурсию
# Оптимизирована, чтобы производить меньше итераций
def sum (a, b):
    max_num = max(a,b)
    min_num = min(a,b)
    if (min_num  == 0): return 1
    return max_num+sum(1, min_num -1)

# Исходные данные
a = 5
b = 7
print(sum(a, b))