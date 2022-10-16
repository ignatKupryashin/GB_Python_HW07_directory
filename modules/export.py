# Должна спросить:
# 1) В какой формат экспортируем
# 2) В как назвать файл, в который экспортируем
# 3) Экспортировать в конкретный формат
from modules.export_modules.xml_generator import create_xml
# from modules.export_modules.txt_generator import create_txt
# from modules.export_modules.csv_generator import create_csv


def export_interface(data):
    while True:
        print("Выберете формат экспорта: \n1: csv\n2: xml\n3: txt")
        export_format = input("Введите цифру:")
        if export_format in ["1", "2", "3"]:
            export(export_format, data)
            break
        else:
            print("Введены некорректные данные")


def export(export_format, data):
    filename = input("Введите имя файла")
    if export_format == 1:
        create_xml(data, filename)

