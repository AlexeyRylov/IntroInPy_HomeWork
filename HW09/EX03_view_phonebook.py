import telebot.types
from telebot import TeleBot
bot = TeleBot('5563677768:AAEGKj3bIt7JCnEdXpDA-PTLyG4utICbejw')


def view_book(phonebook, separator, msg: telebot.types.Message):
    with open(phonebook, 'r', encoding='UTF-8') as pb:
        output_text = ''
        for line in pb:
            if separator in line:
                tmp = line.split(';')
                for i in range(len(tmp)):
                    output_text += tmp[i] + '\n'
        bot.send_message(chat_id=msg.from_user.id, text=output_text)