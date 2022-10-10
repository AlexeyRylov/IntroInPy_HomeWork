'''
Вычислить число π c заданной точностью d
*Пример:* 
- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
'''


def calc_pi(value):
    sum = 0
    i = 0
    while abs(((-1) ** i) / (2 * i + 1)) > value:
        sum += ((-1) ** i) / (2 * i + 1)
        i += 1
    return sum * 4


accuracy = float(input('Введите точноть расчета Пи: '))
if (10 ** (-10)) <= accuracy <= (10 ** (-1)):
    print(calc_pi(accuracy))
else:
    print('точность вне диапазона')