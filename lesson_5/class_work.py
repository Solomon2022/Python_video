# В папке с модулем создать 5 подпапок названия которых состоят
# из платформы на которой запущен интерпритатор и порядковый номер начиная с 1:
# win32_1, win32_2 ... Платформа может быть другой.

import sys, os

name = sys.platform

for i in range(1, 6):
    new_path = os.path.join(os.getcwd(), f'{name}_{i}')
    os.mkdir(new_path)
