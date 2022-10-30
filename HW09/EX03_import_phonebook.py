import os.path
import check_input as ci
import telebot.types
from telebot import TeleBot
bot = TeleBot('5563677768:AAEGKj3bIt7JCnEdXpDA-PTLyG4utICbejw')


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

