# Вводные данные нужны, чтобы пользоваться методом можно было не только для пользователя,
# но и для функции импорта
# если == None  - запускаешь импорты. Если нет - берешь то, что ввели.
# Далее проверяешь валидность в add_note_checker
# **Было бы неплохо добавить ещё проверку на дублирование данных
from modules.add_note_checker import check_tel
import csv


def add_note(family=None, name=None, tel=None, discription=None):
    if family:
        with open("database.csv", "a", newline="") as csvfile:
            fieldnames = ["Фамилия", "Имя", "Телефон", "Описание"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"Фамилия": {family}, "Имя": {name}, "Телефон": {tel}, "Описание": {discription}})
    else:
        dict = {"Фамилия": None, "Имя": None, "Телефон": None, "Описание": None}
        n = 0
        while n == 0:
            family = input("Введите фамилию: ")
            if family.isalpha():
                dict["Фамилия"] = family.capitalize()
                n = 1
            else:
                print("Неверный ввод")
                continue
        while n == 1:
            name = input("Введите имя: ")
            if name.isalpha():
                dict["Имя"] = name.capitalize()
                n = 2
            else:
                print("Неверный ввод")
                continue
        while not tel:
            phone = input("Введите номер телефона: ")
            tel = check_tel(phone)
            if tel:
                dict["Телефон"] = tel
            else:
                print("Неверный ввод")
                continue

        discription = input("Введите описание: ")
        dict["Описание"] = discription.capitalize()

        with open("database.csv", "a", newline="") as csvfile:
            fieldnames = ["Фамилия", "Имя", "Телефон", "Описание"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(dict)