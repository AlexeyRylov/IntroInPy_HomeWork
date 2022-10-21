import check_input as ci


def export_book(phonebook, separator):
    tmp = []
    export_format = 0
    export_name = ''
    export_format = ci.check_num_input('\nВыберите формат записи:\n1 - построчный, 2 - компактный\n', 1, 2)
    export_name = input('Введите имя файла: ')
    if export_format == 1:
        with open(phonebook, 'r', encoding='UTF-8') as pb:
            for line in pb:
                if separator in line:
                    tmp = line.split(';')
                    with open(export_name, 'a', encoding='UTF-8') as ex:
                        ex.write(tmp[0] + '\n' + tmp[1] + '\n' + tmp[2] + '\n' + tmp[3] + '\n')
        print('\nЭкспорт завершен!')
    elif export_format == 2:
        with open(phonebook, 'r', encoding='UTF-8') as pb:
            for line in pb:
                if separator in line:
                    with open(export_name, 'a', encoding='UTF-8') as ex:
                        ex.write(line)
        print('\nЭкспорт завершен!')