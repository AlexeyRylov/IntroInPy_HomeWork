'''
Напишите программу, которая по заданному номеру четверти
показывает диапазон возможных координат точек в этой четверти (x и y).
'''

def coordinatesRange(number):
    if number == 1:
        print(f'в {number} четверти x>0, y>0')
    elif number == 2:
        print(f'во {number} четверти x<0, y>0')
    elif number == 3:
        print(f'в {number} четверти x<0, y<0')
    elif number == 4:
        print(f'в {number} четверти x>0, y<0')
    else:
        print('четверти с таким номером не существует')

quarter = int(input('Введите номер четверти: '))
coordinatesRange(quarter)