"""
------------------------------------------------------------------------------------------------------------------
                                            Семинар 2. Задача №12.
Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю
наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за
прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в
который среднесуточная температура ежедневно превышала 0 градусов Цельсия. 

Напишите программу, помогающую синоптикам в работе. Пользователь вводит число N – общее количество
рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел.
Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в
диапазоне от –50 до 50
------------------------------------------------------------------------------------------------------------------
"""

# Исходные параметры
n = 6
numbers = "-20 30 -40 50 10 -10".split(" ")

length = 0  # Текущая длина последовательности тёплых дней
max_length = 0  # Максимальная длина последовательности тёплых дней

# Вычисление самой длинной оттепели
for i in range(n):
    el = int(numbers[i])

    if el > 0:
        length += 1
    else:
        length = 0

    if length > max_length:
        max_length = length

# Вывод результата
print(f"Самая длинная оттепель длилась: {max_length} дн.")