'''
Задайте список из вещественных чисел. Напишите программу, которая найдёт
разницу между максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''


def sub_digit_minmax(Float_list):
    digit_list = []
    for i in range(len(float_list)):
        tmp = 0
        tmp = round((float_list[i] % 1), 3)
        digit_list.append(tmp)
    print(digit_list)
    min = 0
    min = digit_list[0]
    max = 0
    max = digit_list[0]
    for i in range(len(digit_list)):
        if digit_list[i] < min and digit_list[i] != 0:
            min = digit_list[i]
        if digit_list[i] > max:
            max = digit_list[i]
    return(max - min)


str_list = input('Введите элементы списка через пробел, десятую отделите точкой: ').split()
float_list = [float(x) for x in str_list]
print(sub_digit_minmax(float_list))