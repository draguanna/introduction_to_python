"""
------------------------------------------------------------------------------------------------------------------
                                            Семинар 1. Задача №4. Домашнее задание.
Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали n журавликов.
Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
Выведите через пробел количество журавликов, сделанных Петей, Катей и Сережей.
------------------------------------------------------------------------------------------------------------------
"""
n = 24

# Введите ваше решение ниже

# X+4X+X
x = n / 6
y = 4 * x

print(f'{int(x)} {int(y)} {int(x)}')