'''
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных
aaaaaaaaaaaaaaaaaabbb222aaabbbwwwwwwwwwwwwwwwcc
'''


def compress(tmp_data):
    tmp = []
    count = 1
    for i in range(len(tmp_data) - 1):
        if tmp_data[i] == tmp_data[i + 1]:
            count += 1
        else:
            while count > 9:
                tmp.append('9' + tmp_data[i])
                count -= 9
            else:
                tmp.append(str(count) + tmp_data[i])
            count = 1
        if i == (len(tmp_data) - 2) and tmp_data[i] == tmp_data[i + 1]:
            while count > 9:
                tmp.append('9' + tmp_data[i])
                count -= 9
            else:
                tmp.append(str(count) + tmp_data[i])
        elif i == (len(tmp_data) - 2) and tmp_data[i] != tmp_data[i + 1]:
            tmp.append('1' + tmp_data[i+1])
    # print(tmp)
    return tmp


def decompress(tmp_rle):
    tmp = []
    for i in range(0, len(tmp_rle) - 1, 2):
        tmp.append(str(int(tmp_rle[i]) * tmp_rle[i + 1]))
    # print(tmp)
    with open('HW05_EX04_output', 'w', encoding='UTF-8') as rle:
        rle.write("".join(tmp))
    

with open('HW05_EX04_input', 'w', encoding='UTF-8') as input_data:
    input_data.write('aaaaaaaaaaaaaaaaaaabbb222aaabbbwwwwwwwwwwwwwww  !!!cceeraaaaaaaaaaaaaaaaaaa')
with open('HW05_EX04_input', 'r', encoding='UTF-8') as input_data:
    tmp_data = input_data.readline()
            
with open('HW05_EX04_tmp', 'w', encoding='UTF-8') as rle:
    rle.write("".join(compress(tmp_data)))

with open('HW05_EX04_tmp', 'r', encoding='UTF-8') as input_rle:
    tmp_rle = input_rle.readline()
decompress(tmp_rle)


