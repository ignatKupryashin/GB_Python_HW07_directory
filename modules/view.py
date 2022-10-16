# Прочитать файл database.csv
# Вывести в консоль Фамилия Имя - Телефон - Комментарий
import csv


def view_note():
    with open('database.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row["Фамилия"], row["Имя"], row["Телефон"], row["Описание"])