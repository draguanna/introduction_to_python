"""
------------------------------------------------------------------------------------------------------------------
                                            Семинар 2. Задача №12. Домашнее задание.
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

Примечание: числа S и P задавать не нужно, они будут передаваться в тестах. 
В результате вы должны вывести все возможные пары чисел X и Y через пробел, такие что X <= Y..
------------------------------------------------------------------------------------------------------------------
"""
s = 12
p = 27

# Введите ваше решение ниже

from math import sqrt
# Решение квадратного уравнения
a = 1
b = -s
c = p

# Вычисление дискриминанта
discriminant = b**2 - 4*a*c

# Проверка наличия корней
if discriminant >= 0:
    # Вычисление корней
    root1 = (-b + sqrt(discriminant)) / (2*a)
    root2 = (-b - sqrt(discriminant)) / (2*a)

    # Вывод результатов
    if root1 <= root2:
        print(round(root1), round(root2))
    else: print(round(root2), round(root1))