'''
Задание 3 Задайте список из n чисел последовательности
(1+1/n)^n и выведите на экран их сумму,
округлённую до трёх знаков после точки.
Пример:
Для n = 6 -> 14.072
'''


def function(inputValue):
    tmp = []
    sum = 0
    for i in range(1, inputValue + 1):
        tmp.append((1 + 1 / i) ** i)
        sum += ((1 + 1 / i) ** i)
    return round(sum, 3)


intValue = int(input('Введите число: '))
print(function(intValue))