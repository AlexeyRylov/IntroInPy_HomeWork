from datetime import datetime as dt


def read_data(filename, id):
    with open(filename, 'r', encoding='UTF-8') as rd:
        lines = rd.readlines()
        if len(lines) == 0:
            print('База данных пуста')
            return -1
        else:
            for i in lines:
                if ';' in i:
                    tmp = i.split(';')
                    if tmp[0] == id:
                        tmp[len(tmp) - 1] = tmp[len(tmp) - 1].replace("\n", "")
                        return tmp

def write_data(filename, text1, text2, text3):
    with open(filename, 'r', encoding='UTF-8') as rd:
        lines = rd.readlines()
    input1 = input(text1)
    input2 = input(text2)
    data_ = dt.now().strftime("%Y.%m.%d %H:%M")
    if text3 != '':
        input3 = input(text3)
        lines.append(input1 +';' + input2 + ';' + input3 + ';' + data_ + '\n')
    else:
        lines.append(input1 +';' + input2 + ';' + data_ + '\n')
    with open(filename, 'w', encoding='UTF-8') as wd:
        for i in range(len(lines)):
            wd.write(lines[i])

