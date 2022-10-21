def add_note(phonebook):
    surname = ''
    name = ''
    tel_number = ''
    record_note = ''

    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    tel_number = input('Введите № телефона: ')
    record_note = input('Введите примечание: ')
    
    with open(phonebook, 'a', encoding='UTF-8') as pb:
        pb.write('\n' + surname + ';' + name + ';' + tel_number + ';' + record_note)
    print('\nЗапись добавлена!')