'''
Задание 2 Напишите программу, которая принимает на вход
число N и выдает набор произведений чисел от 1 до N.
Пример:
пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
'''

# Побалуемся рекурсией:
# def fact(inputValue):
#     if inputValue == 1:
#         return 1
#     else:
#         return inputValue * fact(inputValue - 1)


def fact(inputValue):
    tmp = []
    mul = 1
    for i in range(1, inputValue + 1):
        tmp.append(mul * i)
        mul *= i
    return tmp


intValue = int(input('Введите число: '))
print(fact(intValue))
