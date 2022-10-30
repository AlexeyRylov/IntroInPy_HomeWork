import telebot.types
from telebot import TeleBot
bot = TeleBot('5563677768:AAEGKj3bIt7JCnEdXpDA-PTLyG4utICbejw')


export_format = ''
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
