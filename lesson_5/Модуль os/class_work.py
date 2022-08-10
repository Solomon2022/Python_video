import os

# Имя операционной системы
print(os.name)

# Текущая рабочая директория
print(os.getcwd())

# Создаем новый путь и присваиваем его в переменную
new_path = os.path.join(os.getcwd(), '')

# Создаем папку по новому пути
os.mkdir(new_path)

# Удаляем папку
os.rmdir(new_path)