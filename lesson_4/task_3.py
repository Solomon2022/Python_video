# 3: Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health = 100,
# damage = 50. ### Поэкспериментируйте с значениями урона и жизней по желанию.
# ### Теперь надо создать функцию attack(person1, person2). Примечание: имена аргументов можете указать свои.
# ### Функция в качестве аргумента будет принимать атакующего и атакуемого.
# ### В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
# Функция должна сама работать со словарями и изменять их значения.

# 4: Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
# Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно, у вас должно быть 2 функции:
# Наносит урон. Это улучшенная версия функции из задачи 3.
# Вычисляет урон по отношению к броне.
#
# Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья персонажа.

# input('Введите имя первого игрока: ')
player_name = 'Leo'
player = {
    'name' : player_name,
    'health' : 500,
    'damage' : 40,
    'armor' : 1.2
}

# input('Введите имя второго игрока: ')
enemy_name = 'Max'
enemy = {
    'name' : enemy_name,
    'health' : 300,
    'damage' : 50,
    'armor' : 1.5
}

print(f'Игроки: \n{player}\n{enemy}\n')


def armor_func(damage, armor):
    damage /= armor
    return damage


def attack_func(attack, defense):
    damage = attack['damage']
    health = defense['health']
    armor = defense['armor']
    damage = armor_func(damage, armor)
    health -= damage
    health = round(health, 2)
    defense['health'] = health
    return defense


i = 1
while True:
    print(f'Ход № {i}')
    enemy = attack_func(player, enemy)
    if enemy['health'] < 0:
        print(f'{enemy["name"], enemy["health"]}')
        print(f"Победил: {player['name']} !!!")
        break
    player = attack_func(enemy, player)
    if player['health'] < 0:
        print(f'{player["name"], player["health"]}')
        print(f"Победил {enemy['name']} !!!")
        break
    print(f'{enemy["name"], enemy["health"]}')
    print(f'{player["name"], player["health"]}\n')
    i += 1

print()
print(enemy)
print(player)
