'''
Напишите программу для. проверки истинности утверждения
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
'''

def cmpPredicates(input):
    first = not (input[0] or input[1] or input[2])
    second = not input[0] and not input[1] and not input[2]
    if first == second:
        print('Утверждение истинно')
    else:
        print('Утверждение ложно')

strValues = (input('введите значения (0 или 1) для Х, Y, Z, разделенные пробелом: ')).split()
intValues = [int(x) for x in strValues]
cmpPredicates(intValues)
