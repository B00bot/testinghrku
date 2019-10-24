# -*- coding: utf-8 -*-
import config
import telebot
from telebot import types
import random
bot = telebot.TeleBot(config.token)

markup = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('Секрет')
button2 = types.KeyboardButton('Доказательство')
button3 = types.KeyboardButton('Грустно')
button4 = types.KeyboardButton('Памагити')
markup.row(button1, button2, button3)
markup.row(button4)

#stickers for random
stickers = ["CAADAgADCwADlp-MDpuVH3sws_a7FgQ", "CAADAgAD7g0AAqgILwj_8DhBu2dnDRYE", "CAADBAADfQADzjkIDSgZQLclD7jiFgQ", "CAADBAADRAADzjkIDbv4-ULKD6hiFgQ", "CAADAgAD0gIAArnzlwt4AXAE0tVijhYE", "CAADAgAD2gEAAsdjXBUX3pc5V_GYDBYE", "CAADBAADmAADzjkIDRaa2RCZbCJWFgQ", "CAADBAADkwADzjkIDYydFNXPYxHoFgQ", "CAADAgAD4w0AAqgILwh6UH_uBQWn_RYE", "CAADAgADBAgAAhhC7ghzMDDTpZ3HjRYE", "CAADAgADCAADl_TGFHTucAABYtoR1BYE"]

@bot.message_handler(commands=['start'])
def start(message):
    bot.sendMessage(chat_id=message.chat_id, text="Привет, если хочешь узнать тайну, Нажми Секрет Если нужны доказательства - нажми Доказательство. Если грустно - нажми Грустно, если нужна помошь, нажми Памагити")	
    bot.register_next_step_handler(message, menu)
@bot.message_handler(content_types=['text'])
def menu(message: types.Message):
    if message.text.lower()=="секрет":
        bot.sendMessage(chat_id=message.chat_id, text="Мой создатель любит Лапу", reply_markup=markup)
    if message.text.lower()=="памагити":
        bot.sendMessage(chat_id=message.chat_id, text="если хочешь узнать тайну, Нажми Секрет Если нужны доказательства - нажми Доказательство. Если грустно - нажми Грустно, если нужна помошь, нажми Памагити", reply_markup=markup)
    if message.text.lower()=="доказательство":
        randomstick=random.randint(0,10)
        pic=stickers[randomstick]
        bot.sendSticker(chat_id=message.chat_id, sticker=pic, reply_markup=markup)
    if message.text.lower()=="памагити":
        pic=open('s1200.jpeg', 'rb')
        bot.send_photo(chat_id=message.chat_id, photo=pic)
        bot.sendMessage(chat_id=message.chat_id, text="Ни грустииии", reply_markup=markup)

bot.polling(none_stop=true)
bot.idle()
