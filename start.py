from modules.ui import ui
from modules.export import export_interface
# 1) Проверка наличия файла database.csv (если нет - создать файл database.csv)
# 2) Проверка файла database.csv на валидность (пока хз как организовать). Мб, если не валидный - создать файл database1 или что то такое. Тут нужно подумать
# 3) Если всё норм - запустить файл modules/ui.py
print("Телефонный справочник запущен")
try:
    file = open("database.csv")
except:
    file = open("database.csv", "w")
    file.close()

ui()

data = "Фамилия_1,Имя_1,Телефон_1,Описание_1*;***Фамилия_2,Имя_2,Телефон_2,Описание_2*;***"
export_interface(data)