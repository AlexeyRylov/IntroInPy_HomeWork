import os.path


def check_num_input(text, min, max):
    result = 0
    input_ok = False
    while not input_ok:
        try:
            result = int(input(text))
            if min <= result <= max:
                input_ok = True
        except ValueError:
            print('ошибка ввода!')
    return result


def check_file_exist(text):
    result = ''
    input_ok = False
    while not input_ok:
        result = input(text)
        if os.path.exists(result):
            input_ok = True
        else:
            print('Такого файла нет!')
    return result