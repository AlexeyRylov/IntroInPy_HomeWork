'''
Напишите программу, которая принимает на вход координаты двух
точек и находит расстояние между ними в 2D пространстве.
Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
'''

def distance(A, B):
    dist = ((B[1] - A[1]) ** 2 + (B[0] - A[0]) ** 2) ** (0.5)
    return round(dist, 2)

strDotA = (input('введите координаты точки Х, разделенные пробелом: ')).split()
strDotB = (input('введите координаты точки У, разделенные пробелом: ')).split()
intDotA = [int(x) for x in strDotA]
intDotB = [int(x) for x in strDotB]

print(distance(intDotA, intDotB))
