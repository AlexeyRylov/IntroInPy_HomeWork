'''
Напишите программу, которая принимает на вход цифру, обозначающую
день недели, и проверяет, является ли этот день выходным.
Пример:
- 6 -> да
- 7 -> да
- 1 -> нет
'''

DayNumber = int(input('введите номер дня недели: \n'))
if DayNumber == 6 or DayNumber == 7:
       print("да")
elif 1 <= DayNumber <= 6:
    print("нет")
else:
    print("дня с таким номером нет")