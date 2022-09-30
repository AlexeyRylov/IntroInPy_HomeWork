'''
Задание 1 Напишите программу, которая принимает на вход
вещественное число и показывает сумму его цифр.
Пример:
6782 -> 23
0,56 -> 11
'''


strValue = input('Введите вещественное число: ')
sum = 0
for i in range(len(strValue)):
    if strValue[i].isdigit():
        intValue = int(strValue[i])
        sum += intValue
print(f'Сумма чисел равна {sum}')
