"""
------------------------------------------------------------------------------------------------------------------
                                            Семинар 9. Задача 59
1. Проверить есть ли в файле пустые значения
2. Показать median_house_value где median_income < 2
3. Показать данные в первых 2 столбцах
4. Выбрать данные где housing_median_age < 20 и median_house_value > 70000

""" 
# Подключаемые библиотеки
from pandas import read_csv

# Считываем фрейм (объект дата-фрейм)
data = read_csv("california_housing_test.csv")

# 1. Проверить есть ли в файле пустые значения
print(data.isnull().sum())

# 2. Показать median_house_value где median_income < 2
res = data[data["median_income"] < 2]["median_house_value"]
print(res)

# 3. Показать данные в первых 2 столбцах
# Хардкодный способ 
res = data[["longitude","latitude" ]]
print(res)
# Способ через срезв
res = data.iloc[:, :2]
# print(res)

# 4. Выбрать данные где housing_median_age < 20 и median_house_value > 70000
res = data[(data["housing_median_age"] < 20) & (data["median_house_value"] > 70_000)]
print(res)