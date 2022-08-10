# 2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

import random

def random_number():
    return random.randint(1, 100)

a = random_number()
b = random_number()
c = random_number()

def max_number(a, b, c):
    return max(a, b, c)
print(f'Даны три числа: {a}, {b}, {c}')
print('Максимальное из них: ', max_number(a, b, c))
