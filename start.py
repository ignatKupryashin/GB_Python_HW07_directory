from modules.ui import ui
# 1) Проверка наличия файла database.csv (если нет - создать файл database.csv)
# 2) Проверка файла database.csv на валидность (пока хз как организовать). Мб, если не валидный - создать файл database1 или что то такое. Тут нужно подумать
# 3) Если всё норм - запустить файл modules/ui.py
print("Телефонный справочник запущен")
try:
    file = open("database.csv")
except:
    file = open("database.csv", "w+")
    file.close()

ui()