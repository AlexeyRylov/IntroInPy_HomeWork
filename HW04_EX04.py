'''
Задана натуральная степень k. Сформировать случайным образом
список коэффициентов (значения от 0 до 100) многочлена и 
записать в файл многочлен степени k.
Пример:
k=2 => 2*x^2 + 4*x + 5 = 0 или x^2 + 5 = 0 или
10*x^2 = 0
'''


import random


def polinom(size):
    k_list = []
    f = ''
    for i in range(size + 1):
        k_list.append(random.randrange(0, 100))
    print(k_list)
    print(len(k_list))
    
    with open('new_file', 'w', encoding='utf-8') as data:
        for i in range(len(k_list) - 1, -1, -1):
            if k_list[i] != 0 and i >= 2:
                data.write(str(k_list[i]) + '*x^' + str(i) + ' + ')
            if k_list[i] != 0 and i == 1:
                    data.write(str(k_list[i]) + '*x + ')
            if k_list[i] != 0 and i == 0:
                    data.write(str(k_list[i]) + ' = 0')

k = int(input('Введите степень k: '))
polinom(k)