def view_book(phonebook, separator):
    with open(phonebook, 'r', encoding='UTF-8') as pb:
        print('\nТелефонная книга:\n-----------------')
        for line in pb:
            if separator in line:
                tmp = line.split(';')
                for i in range(len(tmp)):
                    print(tmp[i])