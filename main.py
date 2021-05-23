import random
from dict import *
myxp = 0        # переменная для вашего Здоровъя
mydamag = 0     # переменная для вашего урона
mywater = 0     # переменная для вашего Запасов воды
chanse = 30     # Шанс встретить существо
Q = 0           # переменная для генератора случайностей
choice = 0      # переменная существа
animal = 0      # Вид существа
agro = 0        # агресивность существа
xp = 0          # здоровъе существа
damag = 0       # Дамаг существа
loc = 0
popal = 0




def start():
    print('Вы проснулись от громкого крика. Убрав с лица пальмовый лист, вы осмотрелись вокруг.')
    print('Вы увидели лишь тропические заросли, где-то в далеке слышался шум волн.')
    print('Чтобы выйти напишите: выход.')
    global myxp
    myxp = random.randint(7, 10)                # Генерируем Здоровъя у вас
    global mydamag
    mydamag = random.randint(1, 3)              # Генерируем Запасов воды у вас
    global mywater
    mywater = random.randint(20, 27)            # Генерируем вашего урона
    player = input('Будем осматриваться (O) Или уйдём (Enter)?')
    if player == 'O' or player == 'О' or player == '0' or player == 'о' or player == 'o':
        print('Осмотревшись вы выяснили, что')
        print(f'Здоровъя у вас: {myxp} хр')
        print(f'Запасов воды у вас на: {mywater} перемещений')
        print(f'Ваши хилые руки способны нанести: {mydamag} урона')
    else:
        print(f'Вы так и не выяснили своё состояние - Отдавшись на волю случая')
        print(f'Будьте осторожны, подобная небрежность или несмотрительность')
        print(f'Могут стоить вам жизни')
    return


#  Функция снижения количества воды с каждым ходом
def water():
    global myxp
    global mywater
    if mywater >= 1:
        mywater = mywater - 1
        print(f'Запасов воды осталось на: {mywater} перемещений')
    else:
        print(f'Из-за недостатка воды заше здоровье снизилось')
        print(f'Это будет происходить каждых 5 шагов, пока вы не найдёте воду')
        myxp = myxp - 1
        if myxp <= 0:
            print('Вы умерли от жажды. Какая нелепая смерть для такого героя')
            exit()
        mywater = 5
        print(f'У вас осталось: {myxp} хр Здоровъя')
    return


#  Функция генерации минилокации
def gen_loc():
    q = 0           # переменная для генератора случайностей
    global loc        # переменная локации
    q = random.randint(1, 10)  #  Генерируем Шанс попасть в одну из локаций
    if q <= 6:
        loc = 0    # ЧАЩА
    if 6 < q <= 8:
        loc = 1    # Рысья пещера
    if 8 < q <= 10:
        loc = 2    # Берег разбитых кораблей
    print(f'Вы попали в локацию: {loc_dict[loc]}')
    return


#  Функция минилокации Оружейная
def o_loc():
    if loc == 2:        # шанс попасть в локацию с оружейной комнатой
        Q = random.randint(1, 10)
        # print(f'у вас есть шанс попасть в локацию с оружейной комнатой')
        if Q == 1:
            water()
            loc = 3
            print(f'Вы нашли корабль с уцелевшей оружейной комнатой')
            gen_animal(loc)
        elif Q <= 6:
            print(f'Вы видите только пустой пляж')
        else:
            print(f'Вы видите только бесполезные доски от разбившегося корабля')

#  Функция генерации существ
def gen_animal(aloc):
    # print(f'генерируем существо по правилам: {loc_dict[aloc]}')
    global choice               #  переменная существа
    global animal               #  Вид существа
    global agro                 #  агресивность существа
    global xp                   #  здоровъе существа
    global damag                #  Дамаг существа
    q = 0  #  переменная для генератора случайностей
    q = random.randint(0, 100)  #  Генерируем Шанс встретить существо
    if q <= chanse:     # Шанс встретить существо
        #  ЧАЩА
        if aloc == 0:  #  ЧАЩА
            #  Змея(3),Обезъяна(3),БронеЖук(2),КиренРысь(1),Пальмоголовый(1),Пантера(1) = 11
            a = random.randint(1, 11)  #  Генерируем существо
            if a <= 3:#  Змея
                choice = 6
            if 3 < a <= 6:#  Обезъяна
                choice = 7
            if 6 < a <= 8:#  БронеЖук
                choice = 1
            if 8 < a <= 9:#  КиренРысь
                choice = 3
            if 9 < a <= 10:#  Пальмоголовый
                choice = 4
            if 10 < a <= 11:#  Пантера
                choice = 5
        #  Рысья пещера
        if aloc == 1:
            #  Кирена(3),Чихающий еж(3),Пантера(2),Пальмоголовы(1),мартышка(1),бронежук(1) = 11
            a = random.randint(1, 11)  #  Генерируем существо
            if a <= 3:#  Здесь Кирена
                choice = 3
            if 3 < a <= 6:#  Здесь Чихающий Еж
                choice = 7
            if 6 < a <= 8:#  Здесь Пантера
                choice = 2
            if 8 < a <= 9:#  Здесь Пальмоголовий
                choice = 4
            if 9 < a <= 10:#  Здесь  мартышка
                choice = 7
            if 10 < a <= 11:#  Здесь  бронежук
                choice = 1
        #  Берег разбитых кораблей
        if aloc == 2:
            #  Бронежук(3),Змея(1),Обезьяна(1),КиреньРысь(1),Пальмоголовый(1),Пантера(1),ЧихающийЁЖ(1),Шестилап(1),
            a = random.randint(1, 10)  #  Генерируем существо
            if a <= 3:#  Здесь Бронежук
                choice = 1
            if 3 < a <=4:#  Здесь Змея
                choice = 6
            if 4 < a <=5:#  Здесь Обезьяна
                choice = 7
            if 5 < a <=6:#  КиреньРысь
                choice = 3
            if 6 < a <=7:#  Здесь Пальмоголовый
                choice = 4
            if 7 < a <=8:#  Здесь Пантера
                choice = 2
            if 8 < a <=9:#  Здесь ЧихающийЁЖ
                choice = 8
            if 9 < a <=10:#  Здесь Шестилап
                choice = 5
        # Оружейная
        if aloc == 3: # Оружейная
            print(f'Вы нашли корабль с уцелевшей оружейной комнатой')
            # Змея(3),Обезъяна(3),БронеЖук(1) = 7
            a = random.randint(1, 7) #  Генерируем существо
            if a <= 3:
                print('Здесь Змея')
            choice = 6
            if 3 < a <= 6:
                print('Здесь Обезьяна')
            choice = 7
            if 6 < a <= 7:
                print('Здесь Бронежук ')
            choice = 1
        # print(f'Здесь {name[choice]}')
        animal = name[choice]  #  Преобразуем число в название
        agro = status[choice]  #  Преобразуем число в статус
        xp = random.randint(minxp[choice], maxxp[choice])  #  Генерируем xp
        damag = random.randint(mindamag[choice], maxdamag[choice])  #  Генерируем damag
        if agro == 2:
            print(f'{animal} агресивно рычит и собирается напасть')
            print(f'оно будет атаковать с уроном: {damag}')
            print(f'у него: {xp} хр')
            fight()
        else:
            print(f'Просто удивительно, но на вас никто не напал и даже не зарычал')
    return


#  Функция Осмотреться
def lookout():
    if choice != 0:         #  Если существо НЕ "Здесь животных нет" - говорим кого нашли
        if agro == 1:
            print(f'Вы осмотрелись и нашли спокойное {animal}')
            print(f'оно будет защищаться с уроном: {damag}')
            print(f'у него: {xp} хр')
        if agro == 0:
            print(f'Вы осмотрелись и нашли безобидное животное: {animal} оно трусливо убегает')
            print(f'и не будет обороняться')
            print(f'у него: {xp} хр')
        fight()
    else:         #  Если существо "Здесь животных нет" - говорим что НИкого НЕнашли
        print(f'Вы осмотрелись и не нашли существ')
    return


#  Функция Уйти и не Осмотреться
def leave():
    print(f'Вы так и не Осмотрелись - Отдавшись на волю случая')
    print(f'Будьте осторожны, подобная небрежность или несмотрительность')
    print(f'Могут стоить вам жизни')
    return
def B(): # просто надо для завершения цикла
    B = 0
def Bezat(): # Бежать 1 выбор в начале файта
    global myxp
    global animal
    global mydamag
    global xp
    global damag
    print(f"Вы решаете спасаться бегством от {animal}")
    if agro == 2:
        myxp = (myxp - damag) * 2
        print(f"Вы получаете урон от {animal} ! ")
        if myxp < 1:
            print("Ты умер")
            exit()
        else:
            print(f"мое xp {myxp}")
def Bezvat():  # функция определения атаки
    if agro == 2:
        print(f"Атаковать? {animal} с ударом {mydamag}")
        print(f"Бежать? от {animal} то он ударит вас 2 раза с уроном {damag}")

    else:
        print(f"Атаковать? {animal} с ударом {mydamag}")
def Udar(): # Удары
    global myxp
    global animal
    global mydamag
    global xp
    global damag
    global B
        # шанс попасть в существо
    P = random.randint(1,6)
    R = random.randint(1,2)
    B = 0
        # print(f'у вас есть шанс попасть в животное')
    if P == 1 and 6 and 3: #попал
        xp = xp - mydamag
        print(f"Вы пытаетесь ударить животное с уроном {mydamag}")
        print(f"Вы смогли ударить животное {animal} с уроном {mydamag}")
        print(f"Увас здоровья {myxp} Здоровье животного {xp}")
    elif P == 2 and 4 and 5 : #промах
        myxp = myxp - damag
        print(f"Вы пытаетесь ударить животное с уроном {mydamag}")
        print(f"Вы не смогли ударить животное {animal}")
        print(f"Вас бьют с уроном {damag}")
        if myxp <1:
            print("Вы умерли")
        else:
            print(f"Увас здоровья {myxp} Здоровье животного {xp}")
            print(f"Бежать? от {animal} то он может ударить вас с уроном {damag}")
            player = input('Будем Атаковать (Enter) Или Бежать (Б)?')
            if player == 'Б' or player == 'б' or player == 'B' or player == '6':  # Бежать
                if R == 1:
                    print("Вам повезло убежать и остаться целым ")
                    print(f"Увас здоровья {myxp} ")
                    B = 1
                elif R == 2:
                    print(f"Вам не повезло вас ударили с уроном {damag} ")
                    print(f"Увас здоровья {myxp} ")
                    B = 1
                    myxp = myxp - damag
            else:
                print()
def fight(): #Функция битвы
    global myxp
    global animal
    global mydamag
    global xp
    global damag
    global Bezvat
    global Bezat
    global B
    playerAtak = 0
    Bezvat()
    player = input('Будем Атаковать (А) Или Бежать (Enter)?')
    if player == 'A' or player == 'А' or player == 'a' or player == 'а':  # Атаковать
        print(f"Вы решаете атаковать {animal}")
        if agro == 0:
            while myxp >= 1 or xp >= 1:
                xp = xp -mydamag
                myxp = myxp
                print(f"Вы бьете животное с уроном {mydamag}")
                print(f"Увас здоровья {myxp} Здоровье животного {xp}")
                if xp < 1:
                    print("Вы выйграли")
                else:
                    print("Бьемся дальше ")
        elif agro == 1:
            while True:
                Udar()
                if myxp < 1:
                    print("Вы умерли")
                    input()
                    exit()
                elif xp < 1:
                    print("Вы выйграли")
                    print(f"Увас здоровья {myxp} Здоровье животного {xp}")
                    break
                else:
                    if B == 1:
                        break
                    else:
                        print()
        else:
            while True:
                Udar()
                if myxp < 1:
                    print("Вы умерли")
                    input()
                    exit()
                elif xp <1:
                    print("Вы выйграли")
                    break
                else:
                    if B == 1:
                        break
                    else:
                        print()
    else:                                                  #  НЕ Атаковать - Значит сбегаем
        Bezat()
    return

start()         #  Вступление


#  основная программа
while myxp>=1:
    player = input('Ходим (Enter)?')
    if player == 'выход':
        print('Досвидания')
        exit()
    else:
        water()
        gen_loc()
        gen_animal(loc)
        player = input('Будем осматриваться (O) Или уйдём (Enter)?')
        if player == '':
            leave()
        if player == 'O' or player == 'О' or player == '0' or player == 'о' or player == 'o':
            lookout()
            #o_loc()
print('У вас закончились жизни')
exit()

"""
Локация 0 - ЧАЩА
Локация 1 - Рысья пещера
Локация 2 - Берег разбитых кораблей
Локация 3 - Оружейная
Локация 4 - Лагерь туземцев

Начальная локация 0 - ЧАЩА
Большой шанс(3) встретит змею, мартышку
Средний шанс(2) встретить бронежука
Маленький шанс(1) встретить кирену, пальмоголового и пантеру
ПОЛУЧЕНИЕ ПАЛКИ-КОПАЛКИ

Локация 1 - Рысья пещера
Большой шанс встретить - кирену и чихающего ежа
Средний шанс встретить - пантеру и пальмоголового
Маленький шанс встретить - мартышку и бронежука
В пещере находится ценный сундук с САПОГАМИ ПИРАТА
средним кол-вом воды и еды
ПОБЕДИТЬ ТРОИХ КИРЕН

Локация 2 - Берег разбитых кораблей
Большой шанс встретить - бронежука
Средний - никого
Маленький - все остальные
СУНДУК С ИСПАНСКОЙ САБЛЕЙ

Локация 3 - Оружейная
ПОЛУЧЕНИЕ РОБЫ ТУЗЕМЦА

Локация 4 - Лагерь туземцев
Закрытая территория, для получения ЛУКА ТУЗЕМЦА - убить стражника
НЕ ЗАХОДИТЬ НА ТЕРРИТОРИЮ - КОНЕЦ ИГРЫ
Большой шанс встретить - пальмоголового
Средний шанс встретить - пантеру, кирену и бронежука
Маленкий шанс встретить - мартышку, чихающего ежа

changeme( mylist );
"""