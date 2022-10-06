'''
Задайте список из нескольких чисел. Напишите программу, которая
найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''

def odd_sum(value):
    sum = 0
    for i in range(len(value)):
        if i % 2 != 0:
            sum += value[i]
    return sum


str_list = input('Введите элементы списка через пробел: ').split()
int_list = [int(x) for x in str_list]
print(odd_sum(int_list))