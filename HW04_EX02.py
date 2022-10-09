'''
Задайте натуральное число N. Напишите программу,
которая составит список простых множителей числа N.
*Пример*
- при N=236     ->        [2, 2, 59]
'''


def mul_list(value):
    muls = []
    curr_count = 2
    while value != 1:
        if value % curr_count == 0:
            muls.append(curr_count)
            value //= curr_count
        else:
            curr_count +=1
    return muls


number = int(input('Введите число: '))
print(mul_list(number))