# 1: Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py).
# В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из которой запущен данный код.
# Затем создайте вторую функцию удаляющую эти папки.
# Проверьте работу функций в этом же модуле.


import os


def create_dir1_9():
    for i in range(1, 10):
        name = f'dir_{i}'
        os.mkdir(name)


def delete_dir1_9():
    for i in range(1, 10):
        name = f'dir_{i}'
        os.rmdir(name)

if __name__ == '__main__':
    create_dir1_9()
    delete_dir1_9()
