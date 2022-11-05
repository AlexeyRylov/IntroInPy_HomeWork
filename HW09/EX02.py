import telebot.types
from telebot import TeleBot
from datetime import datetime as dt
from time import time
bot = TeleBot('5786145848:AAH4jIafO5fX4CTkKNgiTwZrSdVpwR3S3HM')
number1 = []
number2 = []
math_func = 0

@bot.message_handler(commands=['help'])
def help_command(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="Справка:\n--------------\
                                                    \n/help - cправка\
                                                    \n/add - суммирование чисел\
                                                    \n/sub - вычитание чисел\
                                                    \n/mul - умножение чисел\
                                                    \n/div - деление чисел\
                                                    \n/log - получение лога\
                                                    \n! при вводе чисел через пробел вводятся\
                                                    \n  действительная и мнимая части !")
    log('help', '')


@bot.message_handler(commands=['add'])
def add(msg: telebot.types.Message):
    global math_func
    math_func = 1
    bot.send_message(chat_id=msg.from_user.id, text="Суммирование чисел:\
                                                    \n------------------\
                                                    \nВвод числа 1: ")
    log('add', '')
    bot.register_next_step_handler(msg, input_num1)


@bot.message_handler(commands=['sub'])
def add(msg: telebot.types.Message):
    global math_func
    math_func = 2
    bot.send_message(chat_id=msg.from_user.id, text="Суммирование чисел:\
                                                    \n------------------\
                                                    \nВвод числа 1: ")
    log('sub', '')
    bot.register_next_step_handler(msg, input_num1)


@bot.message_handler(commands=['mul'])
def add(msg: telebot.types.Message):
    global math_func
    math_func = 3
    bot.send_message(chat_id=msg.from_user.id, text="Суммирование чисел:\
                                                    \n------------------\
                                                    \nВвод числа 1: ")
    log('mul', '')
    bot.register_next_step_handler(msg, input_num1)


@bot.message_handler(commands=['div'])
def add(msg: telebot.types.Message):
    global math_func
    math_func = 4
    bot.send_message(chat_id=msg.from_user.id, text="Суммирование чисел:\
                                                    \n------------------\
                                                    \nВвод числа 1: ")
    log('div', '')
    bot.register_next_step_handler(msg, input_num1)


@bot.message_handler(commands=['log'])
def send_log(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text='Лог программы:\
                          \n-------------')
    bot.send_document(chat_id=msg.from_user.id, document=open('log.csv', 'rb'))
    log('log', '')



def input_num1(msg: telebot.types.Message):
    global number1
    input_ok = False
    log('Number 1: ', msg.text)
    while not input_ok:
        number1 = msg.text.split()
        if (len(number1) == 1 and number1[0].isdigit()) or\
            (len(number1) == 2 and number1[0].isdigit() and number1[1].isdigit()):
            input_ok = True
            bot.send_message(chat_id=msg.from_user.id, text="\nВвод числа 2: ")
            bot.register_next_step_handler(msg, input_num2)
        else:
            msg = bot.reply_to(msg, 'Некорректный ввод, попробуйте еще раз:')
            bot.register_next_step_handler(msg, input_num1)
            return


def input_num2(msg: telebot.types.Message):
    global number2
    input_ok = False
    log('Number 2: ', msg.text)
    while not input_ok:
        number2 = msg.text.split()
        if (len(number2) == 1 and number2[0].isdigit()) or\
            (len(number2) == 2 and number2[0].isdigit() and number2[1].isdigit()):
            input_ok = True
            # calculation(number1, number2, msg)
            calculation(msg)
        else:
            msg = bot.reply_to(msg, 'Некорректный ввод, попробуйте еще раз:')
            bot.register_next_step_handler(msg, input_num2)
            return


def calculation(msg: telebot.types.Message):
    global number1
    global number2
    global math_func
    number1 = [int(x) for x in number1]
    number2 = [int(x) for x in number2]
    result = []
    if len(number1) == 1 and len(number2) == 1:
        if math_func == 1:
            result.append(number1[0] + number2[0])
        elif math_func == 2:
            result.append(number1[0] - number2[0])
        elif math_func == 3:
            result.append(number1[0] * number2[0])
        elif math_func == 4:
            result.append(number1[0] / number2[0])
    elif len(number1) == 1 and len(number2) == 2:
        br, bi = number2
        if math_func == 1:
            result.append(number1[0] + br)
            result.append(bi)
        elif math_func == 2:
            result.append(number1[0] - br)
            result.append(bi)
        elif math_func == 3:
            result.append(number1[0] * br)
            result.append(number1[0] * bi)
        elif math_func == 4:
            result.append((ar * br + bi) / (br * br + bi * bi))
            result.append((- ar * bi) / (br * br + bi * bi))
    elif len(number1) == 2 and len(number2) == 1:
        ar, ai = number1
        if math_func == 1:
            result.append(number2[0] + ar)
            result.append(ai)
        elif math_func == 2:
            result.append(number2[0] - ar)
            result.append(ai)
        elif math_func == 3:
            result.append(number2[0] * ar)
            result.append(number2[0] * ai)
        elif math_func == 4:
            result.append(ar / number2[0])
            result.append(ai / number2[0])
    elif len(number1) == 2 and len(number2) == 2:
        ar, ai = number1
        br, bi = number2
        if math_func == 1:
            result.append(ar + br)
            result.append(ai + bi)
        elif math_func == 2:
            result.append(ar - br)
            result.append(ai - bi)
        elif math_func == 3:
            result.append(ar * br - ai * bi)
            result.append(ar * bi + ai * br)
        elif math_func == 4:
            result.append((ar * br + ai * bi) / (br * br + bi * bi))
            result.append((ai * br - ar * bi) / (br * br + bi * bi))
    else:
        return -1
    if len(result) == 1:
        msg = bot.send_message(chat_id=msg.from_user.id, text=f'Результат расчета: {result}\
                                                              \nОжидание команды. Список тут: /help')
    elif len(result) == 2:
        msg = bot.send_message(chat_id=msg.from_user.id, text=f'Результат расчета: {result[0]} + {result[1]}i\
                                                              \nОжидание команды. Список тут: /help')
    log('Result:', f'{result[0]} + {result[1]}i')

def log(func, val):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};{};{}\n'
                    .format(time, func, val))


@bot.message_handler()
def echo(msg: telebot.types.Message):
    bot.reply_to(msg, text="Такой команды нет. Доступные команды тут: /help")
    log(msg.text, '')

 
bot.polling()