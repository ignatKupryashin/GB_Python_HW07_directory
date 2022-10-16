# Должна спросить:
# 1) В какой формат экспортируем
# 2) В как назвать файл, в который экспортируем
# 3) Экспортировать в конкретный формат
import csv
from modules.export_modules.xml_generator import create_xml
from modules.export_modules.txt_generator import create_txt

def export_interface():
    while True:
        print("Выберете формат экспорта: \n1: csv\n2: xml\n3: txt")
        export_format = input("Введите цифру:")
        if export_format in ["1", "2", "3"]:
            export(export_format)
            break
        else:
            print("Введены некорректные данные")


def export(export_format):
    filename = input("Введите имя файла")
    if export_format == "1":
        print("Скоро здесь будет импорт csv")
    if export_format == "2":
        create_xml(filename)
    if export_format == "3":
        create_txt(filename)