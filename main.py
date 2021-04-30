import random
myxp = 0
mydamag = 0
mywater = 0
choice = 0
animal = 0
agro = 0
xp = 0
damag = 0   #Дамаг
chanse = 30   #Шанс встретить существо
Q = 0 #переменная для генератора случайностей
name = {0: 'Никого', 1: 'БронеЖук', 2: 'Пантера', 3: 'КиренРысь', 4: 'Пальмоголовый', 5: 'Шестилап', 6: 'Змея', 7: 'Обезъяна', 8: 'ЧихающийЁЖ'}
status = {0: 0, 1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 1, 7: 1, 8: 0}  #2-агресивный, 1-обороняется, 0-убегает
minxp = {0: 0, 1: 2, 2: 2, 3: 4, 4: 5, 5: 10, 6: 2, 7: 2, 8: 1}
maxxp = {0: 0, 1: 6, 2: 7, 3: 8, 4: 7, 5: 15, 6: 3, 7: 4, 8: 5}
mindamag = {0: 0, 1: 2, 2: 3, 3: 3, 4: 3, 5: 8, 6: 2, 7: 2, 8: 0}
maxdamag = {0: 0, 1: 4, 2: 5, 3: 7, 4: 9, 5: 10, 6: 3, 7: 5, 8: 0}
dict = {1,4,5,6,8,2}

# основная программа
print('Вы проснулись от громкого крика. Убрав с лица пальмовый лист, вы осмотрелись вокруг.')
print('Вы увидели лишь тропические заросли, где-то в далеке слышался шум волн.')
print('Чтобы выйти напишите: выход.')
myxp = random.randint(7, 10)
mydamag = random.randint(1, 3)
mywater = random.randint(20, 27)
player = input('Будем осматриваться?')
if player == 'да' or player == '':
    print('Осмотревшись вы выяснили, что')
    print(f'Здоровъя у вас: {myxp} хр')
    print(f'Запасов воды у вас на: {mywater} перемещений')
    print(f'Ваши хилые руки способны нанести: {mydamag} урона')

while True:
    player = input('Ходим?')
    if player == 'выход':
        print('Досвидания')
        exit()
    Q = random.randint(0, 100)  # Генерируем Шанс встретить существо
    if Q >= chanse:
        print('Здесь животных нет')
    else:
        print('животное сгенерировано')
        choice = random.randint(1, 8)  # Генерируем число
        animal = name[choice]  # Преобразуем число в название
        agro = status[choice]  # Преобразуем число в статус
        xp = random.randint(minxp[choice], maxxp[choice])  # Генерируем xp
        damag = random.randint(mindamag[choice], maxdamag[choice])  # Генерируем damag
        if agro == 2:
            print(f'{animal} агресивно рычит и собирается напасть')
            print(f'оно будет атаковать с уроном: {damag}')
            print(f'у него: {xp} хр')
        else:
            player = input('Будем осматриваться?')
            if player == 'да' or player == '':
                if agro == 1:
                    print(f'Вы нашли спокойное {animal}, но оно будет защищаться')
                    print(f'оно будет защищаться с уроном: {damag}')
                    print(f'у него: {xp} хр')
                if agro == 0:
                    print(f'Вы нашли безобидное животное: {animal} оно трусливо убегает')
                    print(f'и не будет обороняться')
                    print(f'у него: {xp} хр')
print('Закончили')
exit()

# Генерируем update2