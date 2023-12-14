"""
------------------------------------------------------------------------------------------------------------------
                                            Семинар 8. Домашнее задание
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .cvs. Фамилия, имя, отчество, 
номер телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные из файла
2. Программа должна позволять пользователю добавить новую запись в справочник
3. Программа должна сохранять данные в csv файле
4. Должны быть предусмотрены проверки для ФИО и телефона на корректность
5. Использование функций. Ваша программа не должна быть линейной

Домашнее задание: Дополнить справочник возможностью копирования данных из одного файла в другой. 
Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.

"""
# Подключаемые библиотеки
from os.path import exists
from os import stat 
from csv import DictReader, DictWriter
from re import match

# ------------------------- Методы для чтения записей из файла -------------------------
# Проверка существования файла 
def check_file(file_name):
    if (not exists(file_name) or stat(file_name).st_size == 0):
        print(f"Файл {file_name} {'отсутствует' if not exists(file_name) else 'пуст'}. Создайте запись командой w")
        return False
    return True

# Чтение записей из файла (получаем список словарей)
def read_file(file_name):
    with open(file_name, "r", encoding='utf-8') as file:
        f_reader = DictReader(file)
        return list(f_reader)

# Печать списка контактов в консоль
def display_contacts(file_name):
    # Если файл существует и не пустой
    if check_file(file_name):
        user_phones = read_file(file_name)        
        
        # Печать шапки таблицы
        fields = user_phones[0].keys()
        print(f"{'#':<4}", end ='')
        for f in fields: print(f"{f:<15}", end ='')
        print("\n" + "-" * (len(fields) * 15 + 1))

        # Печать контактов
        for i, contact in enumerate(user_phones, start=1):
            print(f"{i:<4}", end ='')
            for f in fields: print(f"{contact.get(f):<15}", end ='')
            print()


# ------------------------- Методы для записи файла -------------------------
# Проверка номера на дубликат
def check_number(file_name, number):
    if exists(file_name) and stat(file_name).st_size != 0:
        user_phones = read_file(file_name)
        for el in user_phones:
            if el["Телефон"] == number:
                print("Такой телефон в справочнике уже есть")
                return False
    return True

# Запись контактов в файл (добавление)
def write_file(file_name, data) :
    # Преобразуем контакт в dict
    obj = {"Фамилия": data[0], "Имя": data[1], "Отчество":data[2], "Телефон": data[3]}

    # Проверяем номер на дубликат
    if not check_number(file_name, str(data[3])): return
 
    # Запись контакта в файл
    with open(file_name, "a", encoding='utf-8', newline='') as file:
        f_writer = DictWriter(file, fieldnames= obj.keys())
        if not exists(file_name) or stat(file_name).st_size == 0: f_writer.writeheader()
        f_writer.writerow(obj)
    print("Контакт успешно добавлен!")

# Ввод имени (фамилии, имени или отчества)
def input_fio(part_of_name):
    while True:
        try:
            input_name = input(f"Введите поле '{part_of_name}': ")
            if not (input_name.isalpha() and len(input_name) >= 2):
                raise ValueError(f"Поле '{part_of_name}' должно состоять только из букв, количество которых не менее 2.")
            return input_name
        except ValueError as err:
            print(err)

# Ввод номера 
def input_number():
    while True:
        try:
            phone_number = input("Введите номер телефона (в формате +7...): ")
            if not match(r"^\+\d{11}$", phone_number):
                raise ValueError("Некорректный номер телефона. Введите в формате +7...")
            return phone_number
        except ValueError as err:
            print(err)

# Ввод контакта
def get_contact():
    # Ввод ФИО
    last_name = input_fio("фамилия")
    first_name = input_fio("имя")
    middle_name = input_fio("отчество")
    
    # Ввод номера
    phone_number = input_number()

    return [last_name, first_name, middle_name, phone_number]

# ------------------------- Методы для копирования контактов -------------------------
# Копирование контакта в файл
def copy_contact(file_name):
    # Если исходный файл существует и не пуст
    if check_file(file_name):
        user_phones = read_file(file_name)
        line_num = int(input("Введите номер строки контакта для копирования в отдельный файл: "))
        
        # Если введённая строка существует в исходном файле
        if (1 <= line_num <= len(user_phones)):
            seen_contact = user_phones[line_num-1]
            new_file_name = seen_contact.get("Телефон")[1:]+'.csv'
            
            #Запись файла
            with open(new_file_name, "w", encoding='utf-8', newline='') as file:
                f_writer = DictWriter(file, fieldnames=seen_contact.keys())
                f_writer.writeheader()
                f_writer.writerow(seen_contact)
            print("Контакт успешно экспортирован")
        else: print("Строки с таким номером в справочнике нет")

# ---------------------- Методы для реализации меню программы-------------------------
# Вывод меню
def show_commands():
        print("\nСПРАВОЧНИК ТЕЛЕФОНОВ")
        print("r - Просмотреть справочник")
        print("w - Добавить новую запись")
        print("c - Копировать контакт в новый файл")
        print("i - Показать список команд")
        print("q - Выход")

# Глобальная переменные
file_name = "phonebook.csv"

# Тело программы
def main():
    show_commands()
    while True:
        command = input("\nВведите команду: ")
        if command == 'r': display_contacts(file_name)
        elif command == 'w': write_file(file_name, get_contact())
        elif command == 'c': copy_contact(file_name)
        elif command == 'i': show_commands()
        elif command == 'q': break 
        else:
            print("Неправильная команда. Попробуйте еще раз.")    
main()