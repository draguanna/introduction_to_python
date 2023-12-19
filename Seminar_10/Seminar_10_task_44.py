"""
------------------------------------------------------------------------------------------------------------------
                                            Семинар 10. Задача 44. Домашнее задание.
Представлен код генерирующий DataFrame, который состоит всего из 1 столбца. 
Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
------------------------------------------------------------------------------------------------------------------
"""
# Подключаемые библиотеки
from pandas import DataFrame, get_dummies, concat
from random import shuffle

# -----------------------------------------------------------------------------------------------------------------
# Методы
# -----------------------------------------------------------------------------------------------------------------

# Генерация дата-фрейма по заданию
def df_generate():
    lst = ['robot'] * 10
    lst += ['human'] * 10
    shuffle(lst)
    data = DataFrame({'whoAmI':lst})
    return data

# Перевод в one hot вид с использованием get_dummies
def oh_encoding_with_get_dummies(data):
    oh_data = get_dummies(data['whoAmI'])
    return oh_data

# Перевод в one hot вид без использования get_dummies
def oh_encoding_custom_method(data):
    unique_values = data['whoAmI'].unique()
    oh_data = DataFrame(columns=unique_values)
    for value in unique_values:
        oh_data[value] = data['whoAmI'].apply(lambda x: 1 if x == value else 0)
    return oh_data

# -----------------------------------------------------------------------------------------------------------------
# Тело программы
# -----------------------------------------------------------------------------------------------------------------

# Генерация дата-фрейма
data = df_generate()

# Перевод в one hot вид с использованием get_dummies
oh_data_1 = oh_encoding_with_get_dummies(data)
res_data_1 = concat([data, oh_data_1], axis=1)
print(f"\n{res_data_1.head(5)}")

# Перевод в one hot вид без использования get_dummies
oh_data_2 = oh_encoding_custom_method(data)
res_data_2 = concat([data, oh_data_2], axis=1)
print(f"\n{res_data_2.head(5)}")
