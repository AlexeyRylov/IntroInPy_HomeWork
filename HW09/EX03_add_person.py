import telebot.types
from telebot import TeleBot
bot = TeleBot('5563677768:AAEGKj3bIt7JCnEdXpDA-PTLyG4utICbejw')


def add_note(msg: telebot.types.Message):
    with open('HW07_phonebook', 'a', encoding='UTF-8') as pb:
        pb.write('\n' + msg.text)
    bot.send_message(chat_id=msg.from_user.id, text="Запись добавлена!")
