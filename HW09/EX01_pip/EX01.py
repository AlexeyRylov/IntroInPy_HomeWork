import random
import emoji
from emoji import emojize as emo


def print_field(lis: list):
    for i in range(3):
        print(f'{lis[0 + i * 3]}\t{lis[1 + i *3]}\t{lis[2 + i * 3]}')


def change_player(curr_player):
    if curr_player == 1:
        return 2
    else:
        return 1


def player_input(play_field, curr_player, player_symbol):
    input_ok = False
    while not input_ok:
        try:
            player_input = int(input(f'Ход игрока {curr_player}: '))
        except:
            print('Повтор ввода: ')
            continue
        if player_input >= 1 and player_input <= 9:
            if not emoji.is_emoji(play_field[player_input - 1]):
                play_field[player_input - 1] = player_symbol
                input_ok = True
            else:
                print('Упс, поле занято')
        else:
            print('Упс, поля с таким номером нет')


def vin_combinations(play_field: list):
    combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (2, 4, 6), (0, 4, 8))
    for i in combinations:
        if play_field[i[0]] == play_field[i[1]] == play_field[i[2]]:
            return play_field[i[0]]
    return False


def engine():
    curr_player = random.randrange(1, 3)
    print(f'Жеребьевка завершена! Игрок {curr_player} начинает первым!')
    step = 0
    victory = False
    play_field = [x for x in range(1, 10)]
    while not victory:
        if step != 0:
            curr_player = change_player(curr_player)
        print_field(play_field)
        if curr_player == 1:
            player_symbol = f'{emo(":cross_mark:", variant = "emoji_type")}'
        else:
            player_symbol = f'{emo(":hollow_red_circle:")}'
        player_input(play_field, curr_player, player_symbol)
        step += 1
        if step >= 5:
            temp = vin_combinations(play_field)
            if temp:
                print(f'\nИгрок {curr_player} победил\n')
                victory = True
                break
        if step == 9:
            print('Победила дружба')
            break
    print_field(play_field)


engine()