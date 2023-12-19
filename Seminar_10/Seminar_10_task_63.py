"""
                                            Семинар 10. Задача 63.
1. Изобразите отношение households к population с помощью точечного графика
2. Визуализировать longitude по отношения к median_house_value, используя линейный график
3. Представить гистограмму по housing_median_age
4. Изобразить гистограмму по median_house_value с оттенком housing_median_age

"""
# Подключаемые библиотеки
from pandas import read_csv
from seaborn import scatterplot, relplot, histplot
from matplotlib.pyplot import show

# Загрузка данных из файла california_housing_train.csv
data = read_csv('california_housing_test.csv')

#1. Изобразите отношение households к population с помощью точечного графика
def first(data):
    scatterplot(data=data, x='households', y='population')
    show()

#2. Визуализировать longitude по отношения к median_house_value, используя линейный график
def second(data):
    relplot(x="longitude", y="median_house_value", kind="line", data=data)
    show()

#3. Представить гистограмму по housing_median_age
def third(data):
    histplot(data=data, x="housing_median_age")
    show()

# 4. Изобразить гистограмму по median_house_value с оттенком housing_median_age
def fourth(data):
    histplot(data=data, x="median_house_value", hue="housing_median_age")
    show()

fourth(data)