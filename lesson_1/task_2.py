# 2: Используя цикл, запрашивайте у пользователя число, пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степень 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число неверное, и говорите о диапазоне допустимых. И просите ввести заново.
# Допустим, пользователь ввел 2, оно подходит. Возводим его в степень 2 и выводим 4.

number = int(input("Введите число: "))
while not (number > 0 and number < 10):
    print("Неверно! Число должно быть больше 0, но меньше 10.")
    number = int(input("Введите число: "))
number **= 2
print("Число в квадрате", number)