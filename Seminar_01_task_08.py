"""
------------------------------------------------------------------------------------------------------------------
                                            Семинар 1. Задача №8. Домашнее задание.
Определите, можно ли от шоколадки размером a × b долек отломить c долек, если разрешается сделать один разлом по 
прямой между дольками (то есть разломить шоколадку на два прямоугольника).
Выведите yes или no соответственно.
------------------------------------------------------------------------------------------------------------------
"""

a = 3
b = 2
c = 4

# Введите ваше решение ниже

min_value = min(a,b)
max_value = max((a-1)*b,(b-1)*a)
print("yes" if (c >= min_value and c <= max_value)  else "no")