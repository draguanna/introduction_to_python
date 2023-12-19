"""
                                            Семинар 10. Задача 69.
Изобразить гистограмму по flipper_length_mm с оттенком height_group.
Сделать анализ
"""

# Подключаемые библиотеки
from pandas import read_csv
from seaborn import histplot
from matplotlib.pyplot import show

# Загрузка данных из файла penguins.csv
penguins = read_csv('penguins.csv')

def hist():
    histplot(data=penguins, x="flipper_length_mm", hue="height_group")
    show()

hist()