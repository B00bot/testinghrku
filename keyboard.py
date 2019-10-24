import telebot
from telebot import types

keyb = types.ReplyKeyboardMarkup(True, False)
keyb.row('Секрет', 'Доказательство','Грустно')
keyb.row('Нипанятнаа')
