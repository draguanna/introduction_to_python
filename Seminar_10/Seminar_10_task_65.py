"""
                                            Семинар 10. Задача 65.
Написать EDA для датасета про пингвинов. Необходимо:
● Использовать 2-3 точечных графика
● Применить доп измерение в точечных графиках, используя аргументы hue, size, stile
● Использовать PairGrid с типом графика на ваш выбор
● Изобразить Heatmap
● Использовать 2-3 гистограммы

Чтобы подключить датасет с пингвинами, воспользуйтесь данным скриптом: 
    penguins = sns.load_dataset("penguins")
    penguins.head()
"""
# Подключаемые библиотеки
from seaborn import load_dataset, scatterplot, PairGrid, heatmap
from matplotlib.pyplot import show, xlabel, ylabel

# Загрузка данных
penguins = load_dataset("penguins")
print(penguins.head())

# Использовать 2-3 точечных графика
def f_1():
    scatterplot(data=penguins, x="flipper_length_mm", y="body_mass_g")
    show()

# Применить доп измерение в точечных графиках, используя аргументы hue, size, stile
def f_2():
    scatterplot(data=penguins, x="flipper_length_mm", y="body_mass_g", hue='sex', size='island', style='island')
    show()

# Использовать PairGrid с типом графика на ваш выбор
def f_3():
    x_vars = ["body_mass_g", "bill_length_mm", "bill_depth_mm", "flipper_length_mm"]
    y_vars = ['sex']
    pg = PairGrid(penguins, x_vars=x_vars, y_vars=y_vars, hue='species')
    pg.map(scatterplot)
    show()

# Изобразить Heatmap
def f_4():
    data = penguins.pivot_table(index='species', columns='island', values='body_mass_g')
    heatmap(data)
    xlabel('Остров', size=14)
    ylabel('Вид пингвина', size=14)
    show()

# Использовать 2-3 гистограммы
def f_5():
    penguins['bill_depth_mm'].hist(bins=15)
    show()


f_1()
f_2()
f_3()
f_4()
f_5()
