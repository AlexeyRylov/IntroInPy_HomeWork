import EX03_view_phonebook as vp
import EX03_add_person as ap
import EX03_export_phonebook as ep
import EX03_import_phonebook as ip
import telebot.types
from telebot import TeleBot, types
import os.path
phonebook = 'HW07_phonebook'
separator = ';'
bot = TeleBot('5563677768:AAEGKj3bIt7JCnEdXpDA-PTLyG4utICbejw')


@bot.message_handler(commands=['help'])
def help_command(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="Справка:\n--------------\
                                                    \n/help - cправка\
                                                    \n/view - просмотр книги\
                                                    \n/add - добавление записи\
                                                    \n/export - экспорт книги\
                                                    \n/import - импорт книги")

@bot.message_handler(commands=['view'])
def view_command(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="Телефонная книга:\n------------------------------")
    vp.view_book(phonebook, separator, msg)

@bot.message_handler(commands=['add'])
def add_note(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="Добавление пользователя:\
                                                    \n-------------------------------------------\
                                                    \nВведите Фамилию: ")
    bot.register_next_step_handler(msg, add_note)

input_data = []
def add_note(msg: telebot.types.Message):
    global input_data
    input_data.append(msg.text)
    msg = bot.send_message(chat_id=msg.from_user.id, text='Введите имя: ')
    bot.register_next_step_handler(msg, add_note_1)


def add_note_1(msg: telebot.types.Message):
    global input_data
    input_data.append(msg.text)
    msg = bot.send_message(chat_id=msg.from_user.id, text='Введите № телефона: ')
    bot.register_next_step_handler(msg, add_note_2)

def add_note_2(msg: telebot.types.Message):
    global input_data
    input_data.append(msg.text)
    msg = bot.send_message(chat_id=msg.from_user.id, text='Введите примечание к записи: ')
    bot.register_next_step_handler(msg, add_note_3)

def add_note_3(msg: telebot.types.Message):
    global input_data
    input_data.append(msg.text)
    with open('HW07_phonebook', 'a', encoding='UTF-8') as pb:
        pb.write('\n' + input_data[0] + ';'\
                      + input_data[1] + ';'\
                      + input_data[2] + ';'\
                      + input_data[3])
    bot.send_message(chat_id=msg.from_user.id, text="Запись добавлена!")
    input_data = []


@bot.message_handler(commands=['export'])
def view_command(msg: telebot.types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('построчный', 'компактный')
    msg = bot.reply_to(msg, 'Экспорт книги:\n-------------------------\
                            \nВыберите формат записи:\n1 - построчный, 2 - компактный\n', reply_markup=markup)
    bot.register_next_step_handler(msg, export_book)

export_format = ''
def export_book(msg: telebot.types.Message):
    global export_format
    export_format = msg.text
    msg = bot.send_message(chat_id=msg.from_user.id, text='Введите имя файла: ')
    bot.register_next_step_handler(msg, export_book_1)

def export_book_1(msg: telebot.types.Message):
    tmp = []
    export_name = msg.text
    if export_format == u'построчный':
        with open('HW07_phonebook', 'r', encoding='UTF-8') as pb:
            for line in pb:
                if ';' in line:
                    tmp = line.split(';')
                    with open(export_name, 'a', encoding='UTF-8') as ex:
                        ex.write(tmp[0] + '\n' + tmp[1] + '\n' + tmp[2] + '\n' + tmp[3] + '\n')
        msg = bot.send_message(chat_id=msg.from_user.id, text='Экспорт завершен!')
    elif export_format == u'компактный':
        with open('HW07_phonebook', 'r', encoding='UTF-8') as pb:
            for line in pb:
                if ';' in line:
                    with open(export_name, 'a', encoding='UTF-8') as ex:
                        ex.write(line)
        msg = bot.send_message(chat_id=msg.from_user.id, text='Экспорт завершен!')


@bot.message_handler(commands=['import'])
def view_command(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="Импорт книги:\n------------------------\
                                                    \nВведите имя файла:")
    bot.register_next_step_handler(msg, import_book)

def import_book(msg: telebot.types.Message):
    input_ok = False
    while not input_ok:
        filename = ''
        filename = msg.text
        if os.path.exists(filename):
            input_ok = True
        else:
            msg = bot.reply_to(msg, 'Такого файла нет, введите еще раз:')
            bot.register_next_step_handler(msg, import_book)
            return
    with open(filename, 'r', encoding='UTF-8') as source:
        for line in source:
            if ';' in line:
                with open('HW07_phonebook', 'a', encoding='UTF-8') as pb:
                    pb.write(line)
        msg = bot.send_message(chat_id=msg.from_user.id, text='Импорт завершен!')


@bot.message_handler()
def echo(msg: telebot.types.Message):
    bot.reply_to(msg, text="Такой команды нет. Доступные команды тут: /help")
 
bot.polling()