'''
Реализуйте алгоритм перемешивания списка
'''


import random


def mixList(userList):
    result = []
    tmp = userList
    currPos = 0
    for i in range(len(userList)):
        currPos = random.randrange(0, len(tmp))
        result.append(userList[currPos])
        tmp.pop(currPos)
    return result


size = int(input('Введите размерность списка: '))
if size < 0:
    print('Размер списка не может быть отрицательным!')
else:
    userList = []
    for i in range(size):
        userList.append(i)
    print(f'Исходный список: \t {userList}')
    print(f'Перемешанный список: \t {mixList(userList)}')