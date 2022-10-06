'''
Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''


def mul_pairs(value):
    result = []
    even_number = False
    if len(value) % 2 == 0:
        for i in range(int(len(value) / 2)):
            result.append(value[i] * value[(len(value) - i - 1)])
    else:
        for i in range(int(len(value) / 2) + 1):
            result.append(value[i] * value[(len(value) - i - 1)])
    return result


str_list = input('Введите элементы массива через пробел: ').split()
int_list = [int(x) for x in str_list]
print(mul_pairs(int_list))