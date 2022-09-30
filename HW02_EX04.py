'''
Задание 4 Задайте список из N элементов, заполненных числами
из промежутка [-N, N]. Найдите произведение элементов на
позициях a и b. Значения N, a и b вводит пользователь с клавиатуры.
'''

def function(intValues):
    tmp = []
    for i in range(-intValues[0], intValues[0] + 1):
        tmp.append(i)
    return (tmp[intValues[1]] * tmp[intValues[2]])


strValues = (input('введите значения N, a и b, разделенные пробелом: ')).split()
intValues = [int(x) for x in strValues]

if (intValues[1] < 0) or (intValues[1] > (intValues[0] * 2)):
    print('значение a вне диапазона')
elif (intValues[2] < 0) or ((intValues[2] > intValues[0] * 2)):
    print('значение b вне диапазона')
else:
    print(function(intValues))