'''
Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять
первому игроку, чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом""
'''

import random
candy_num = 2021
step_max = 28


def change_player(curr_player):
    if curr_player == 1:
        return 2
    else:
        return 1


def engine(candy_num, step_max, bot_en):
    curr_player = random.randrange(1, 3)
    print(f'Жеребьевка завершена! Игрок {curr_player} начинает первым!')

    step = 0
    while candy_num > 0:
        if step != 0:
            curr_player = change_player(curr_player)
        if curr_player == 1 or (curr_player == 2 and bot_en == False):
            curr_num = int(input(f'Игрок {curr_player}: ввод забираемых конфет: '))
        else:
            curr_num = candy_num % (step_max + 1)
            print(f'Игрок {curr_player}: ввод забираемых конфет: {curr_num}')


        while curr_num <= 0 or curr_num > step_max or curr_num > candy_num:
            curr_num = int(input(f'Игрок {curr_player}: повтор ввода: '))
        else:
            candy_num -= curr_num
            step +=1
            print(f'Осталось {candy_num} конфет')
    else:
        print(f'Игра завершена! Победил Игрок {curr_player}')


welcome = 0
while welcome > 2 or welcome < 1:
    welcome = int(input('Привет, играем с ботом? 1 - ДА, 2 - НЕТ: '))
else:
    if welcome == 1:
        bot_en = True
    else:
        bot_en = False

engine(candy_num, step_max, bot_en)

    

