'''
Напишите программу, которая будет преобразовывать
десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
'''


def dec_to_bin(value):
    tmp = []
    while value >= 2:
        tmp.append(value % 2)
        value = value // 2
    tmp.append(value)
    tmp.reverse()
    for i in range(len(tmp)):
        print(tmp[i], end='')


decimal_number = int(input('Введите целочисленное десятичное число: '))
dec_to_bin(decimal_number)