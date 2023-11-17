"""
------------------------------------------------------------------------------------------------------------------
                                            Семинар 1. Задача №6. Домашнее задание.
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.
------------------------------------------------------------------------------------------------------------------
"""

n = 385916

# Введите ваше решение ниже

# Разбиваем номер билета на отдельные цифры
digits = [int(digit) for digit in str(n)]
print("yes" if sum(digits[:3]) == sum(digits[3:]) else "no")