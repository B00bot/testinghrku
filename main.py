# coding=utf-8
import telebot
from telebot import types

TOKEN = '971858815:AAGd5HKRgTmUFpaxo4S4szOmonfA0T0EZqI'

bot = telebot.TeleBot(TOKEN)
    
    @bot.message_handler(commands=['start'])
def startpg(message):
    startmenu = types.ReplyKeyboardMarkup(True, False)
    startmenu.row('Секрет', 'Доказательство')
    startmenu.row('Грустно')
    startmenu.row('Нипанятнаа')
    bot.send_message(message.chat.id, 'Привет. Есзи хочешь узнать секрет, нажми секрет. Если нужно доказательство, нажми Доказательство. Если грустно, нажми Грустно. Если нужна помошь - нажми Нипанятнаа', reply_markup=startmenu)
    
    bot.polling()
    
