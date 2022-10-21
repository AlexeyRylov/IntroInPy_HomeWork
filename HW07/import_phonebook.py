import os.path
import check_input as ci


def import_book(phonebook, separator):
    tmp = []
    count = 0
    filename = ci.check_file_exist('Введите имя файла импорта: ')
    with open(filename, 'r', encoding='UTF-8') as source:
        for line in source:
            if separator in line:
                with open(phonebook, 'a', encoding='UTF-8') as pb:
                    pb.write(line)
            # elif line != '':
            #     tmp.append(line)
            #     print(line)
            #     count +=1
        
        # old = ''
        # new_note = True
        # for i in range(len(tmp)):
        #     if tmp[i] != ' ' and new_note:
        #         with open(phonebook, 'a', encoding='UTF-8') as pb:
        #             pb.write(tmp[i])
        print('\nИмпорт завершен!')
