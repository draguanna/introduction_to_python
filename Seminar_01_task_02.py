"""
------------------------------------------------------------------------------------------------------------------
                                            Семинар 1. Задача №2. Домашнее задание.
Найдите сумму цифр трехзначного числа n. Результат сохраните в перменную res.
------------------------------------------------------------------------------------------------------------------
"""
n = 135

# Введите ваше решение ниже
res = 0
while (n > 0):
    digit = n % 10
    res += digit
    n //= 10

print(res)