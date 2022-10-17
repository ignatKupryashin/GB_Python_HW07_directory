from modules.view import view_note
from modules.add_note import add_note
from modules.export import export_interface
from modules.import_module import import_interface


def ui():
    while True:
        print("")
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
        if number not in [1, 2, 3, 4, 9]:
            print("Неверный ввод, повторите попытку")
            continue

        if number == 1:
            view_note()

        if number == 2:
            add_note()

        if number == 3:
            export_interface()

        if number == 4:
            import_interface()

        if number == 9:
            print("Хорошего дня!")
            return
