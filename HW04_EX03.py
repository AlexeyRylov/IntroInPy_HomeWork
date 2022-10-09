'''
Задайте последовательность чисел. Напишите программу,
которая выведет список неповторяющихся элементов
исходной последовательности.
*Пример*
- при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->
        [2, 4, 5, 9]
'''


def unrep_elems(value):
    result = [x for x in value if value.count(x) < 2]
    return result


str_input = input('Введите последовательность чисел, разделите их пробелом: ').split()
int_input = [int(x) for x in str_input]
print(unrep_elems(int_input))
