import random
choice = 0
animal = 0
agro = 0
xp = 0
damag = 0
name = {0: 'Никого нет', 1: 'БронеЖук', 2: 'Пантера', 3: 'КиренРысь', 4: 'Пальмоголовый', 5: 'Шестилап', 6: 'Змея', 7: 'Обезъяна', 8: 'ЧихающийЁЖ'}
status = {0: 0, 1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 1, 7: 1, 8: 0}
minxp = {0: 0, 1: 2, 2: 2, 3: 4, 4: 5, 5: 10, 6: 2, 7: 2, 8: 1}
maxxp = {0: 0, 1: 6, 2: 7, 3: 8, 4: 7, 5: 15, 6: 3, 7: 4, 8: 5}
mindamag = {0: 0, 1: 2, 2: 3, 3: 3, 4: 3, 5: 8, 6: 2, 7: 2, 8: 0}
maxdamag = {0: 0, 1: 4, 2: 5, 3: 7, 4: 9, 5: 10, 6: 3, 7: 5, 8: 0}



# основная программа
while True:
    print('Играем в Bыживание. Чтобы выйти напишите: выход.')
    player = input('Играем?:')
    if player == 'выход':
        print('Досвидания')
        exit()
    choice = random.randint(0, 8)  # Генерируем
    animal = name[choice]  # Преобразуем в название
    agro = status[choice]  # Преобразуем в стоимость
    xp = random.randint(minxp[choice], maxxp[choice])  # Генерируем
    damag = random.randint(mindamag[choice], maxdamag[choice])  # Генерируем
    print(f'Вы встретили: {animal}')
    print(f'xp: {xp}')
    print(f'damag: {damag}')
print('Закончили')
exit()
