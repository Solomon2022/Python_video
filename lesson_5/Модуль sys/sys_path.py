# мы можем импортировать
import math
# но не можем импортировать наш модуль например на диске С:
# import my_module

# Как python находит модули?
import sys
print(sys.path)
print(type(sys.path))
print()

# Добавим в python путь к своему модулю и импортируем его
sys.path.append('D:\Рабочий стол')
import my_module

for el in sys.path:
    print(el)