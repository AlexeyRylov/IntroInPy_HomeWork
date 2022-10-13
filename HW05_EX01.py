'''
Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
'''

with open('HW05_EX01', 'w', encoding='UTF-8') as data_file:
    data_file.write('абв еее жук ввв абв крн ывп')
with open('HW05_EX01', 'r', encoding='UTF-8') as data_file:
    input_data = data_file.readline().split()

output_data = list(filter(lambda x: 'абв' not in x, input_data))

with open('HW05_EX01', 'w', encoding='UTF-8') as data_file:
    data_file.write(" ".join(output_data))