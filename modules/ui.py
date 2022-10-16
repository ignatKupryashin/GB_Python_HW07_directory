from modules.view import view_note
from modules.add_note import add_note
from modules.export import export_interface
# меню программы
# Предлагаю реализовывать в бесконечном цикле
# Должна поздороваться, вывести меню и принять от пользователя цифру:
# Если не та цифра - повторить. Если та - вызываем соответствующую функцию из соответствующего файла.
# Пока у нас нет имён методов - оставляй поле пустым. Как будут наименования методов - заполним
# При выборе цифры 9 - выход из программы. Попрощаться и break


def ui():
    number = None
    while number != 9:
        print("МЕНЮ:")
        print("1: Посмотреть все записи")
        print("2: Добавить запись")
        print("3: Экспорт")
        print("4: Импорт")
        print("9: Выход")

        number = input("Введите пункт меню: ")
        if number.isdigit():
            number = int(number)
        else:
            print("Неверный ввод, повторите попытку")
            continue
        if number < 0 or number > 9:
            print("Неверный ввод, повторите попытку")
            continue

        if number == 1:
            view_note()

        if number == 2:
            add_note()

        if number == 3:
            export_interface()