"""
------------------------------------------------------------------------------------------------------------------
                                            Семинар 2. Задача №9.
По данному целому неотрицательному n вычислите значение n!. 
N! = 1 * 2 * 3 * … * N  (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
------------------------------------------------------------------------------------------------------------------
"""
# Исходные параметры
n = 5

# Вычисление результата
factorial = 1
while n > 1:
    factorial *= n
    n -= 1

# Вывод результата
print(f"{n}! = {factorial}")