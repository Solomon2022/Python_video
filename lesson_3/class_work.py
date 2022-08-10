import random

print("Игра угадай число!!!")
comp_number = random.randint(1, 100)
user_number = None

count = 0
levels = {1: 10, 2: 5, 3: 3}
max_count = levels[int(input("Выберите уровень сложности: "))]

users_list = []
for el in range(int(input("Введите количество игроков: "))):
    users_name = input(f"Введите имя игрока {el + 1}: ")
    users_list.append(users_name)
print(users_list)

is_winner = False
winner_name = None

while not is_winner:
    count += 1
    if count > max_count:
        print("Все игроки проиграли!!!")
        break
    print(f"Попытка № {count}")
    for el in users_list:
        user_number = int(input(f"Введите число ({el}): "))
        if user_number == comp_number:
            is_winner = True
            winner_name = el
            break
        elif user_number < comp_number:
            print("Ваше число меньше!")
        else:
            print("Ваше число больше!")
    print()
else:
    print(f"Победил {winner_name}!!!")
