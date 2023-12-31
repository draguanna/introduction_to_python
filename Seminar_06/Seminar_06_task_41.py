"""
------------------------------------------------------------------------------------------------------------------
                                            Семинар 6. Задача 41.
Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, 
у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится число N — количество 
элементов в массиве Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.
------------------------------------------------------------------------------------------------------------------
"""

# Исходные данные
lst = [1, 5, 1, 5, 1]

# Функция подсчета элементов, удовлетворяющих условию
def counting(lst):
    count = 0
    for i in range(1, len(lst)-1):
        if (lst[i-1] < lst[i] and lst[i+1] < lst[i]): count+=1
    return count

# Вывод результата
print(f"Кол-во элементов: {counting(lst)}")