'''
Задайте число. Составьте список чисел Фибоначчи,
в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так:
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
'''


def fibonacci(value):
    tmp = []
    for n in range(value * 2 + 1):
        tmp.append(0)
    i = 0
    i = value
    for i in range(value + 1):
        if i == 0:
            tmp[value] = 0
        elif i == 1:
            tmp[value + 1] = 1
            tmp[value - 1] = 1
        else:
            tmp[value + i] = tmp[value + i - 2] + tmp[value + i -1]
            if i % 2 == 0:
                tmp[value - i] = -1 * (abs(tmp[value + i - 2]) + abs(tmp[value + i -1]))
            else:
                tmp[value - i] = abs(tmp[value + i - 2]) + abs(tmp[value + i -1])
    print(tmp)


number = int(input('Введите вычисляемую глуину ряда Фибоначчи: '))
fibonacci(number)
