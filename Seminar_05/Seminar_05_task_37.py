"""
------------------------------------------------------------------------------------------------------------------
                                            Семинар 5. Задача 37.
Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в
обратном порядке. Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
------------------------------------------------------------------------------------------------------------------
"""
# Исходные данные
num = 3

# Функция записывает последовательность в обратном порядке
def reverse (n):
    if (n > 0): 
        num = int(input("Введите число: "))
        reverse(n-1)
        print(num, end=' ')

# Вывод результата
reverse(num)
