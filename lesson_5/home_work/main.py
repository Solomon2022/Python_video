# 3: Создайте модуль main.py. Из модулей реализованных в заданиях 1 и 2 сделайте импорт в main.py всех функций.
# Вызовите каждую функцию в main.py и проверьте что все работает как надо.
# Примечание: Попробуйте импортировать как весь модуль целиком (например из задачи 1), так и отдельные функции из модуля.

import module_task_2
from module_task_1 import create_dir1_9, delete_dir1_9


create_dir1_9()
delete_dir1_9()

print(module_task_2.random_list([1, 2, 3, 4, 5]))
print(module_task_2.random_list([]))