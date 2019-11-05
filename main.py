import os

import telebot
from telebot import types
from config import *
from config import TOKEN
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import random
import keyboard
from keyboard import keyb
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)
app = Flask(__name__)
db = SQLAlchemy(app)

stickers = ["CAADAgADCwADlp-MDpuVH3sws_a7FgQ", "CAADAgAD7g0AAqgILwj_8DhBu2dnDRYE", "CAADBAADfQADzjkIDSgZQLclD7jiFgQ", "CAADBAADRAADzjkIDbv4-ULKD6hiFgQ", "CAADAgAD0gIAArnzlwt4AXAE0tVijhYE", "CAADAgAD2gEAAsdjXBUX3pc5V_GYDBYE", "CAADBAADmAADzjkIDRaa2RCZbCJWFgQ", "CAADBAADkwADzjkIDYydFNXPYxHoFgQ", "CAADAgAD4w0AAqgILwh6UH_uBQWn_RYE", "CAADAgADBAgAAhhC7ghzMDDTpZ3HjRYE", "CAADAgADCAADl_TGFHTucAABYtoR1BYE"]

@bot.message_handler(commands=['start'])
def start_message(msg):
    bot.send_message(msg.chat.id, """Если хочешь узнать тайну, нажми ❤️ Секрет ❤️ 
Если нужны доказательства
нажми 😘 Докажи 😘 
Если грустно
нажми 😞 Грустно 😞 
Если ничего не понятно
нажми 🤷‍♂️ Нипанятнаа 🤷‍♂️""", reply_markup=keyb)

@bot.message_handler(content_types=['text'])
def amy_message(msg):
    if msg.text.lower() == '❤️ секрет ❤️':
        bot.reply_to(msg, "Мой создатель любит тебя", reply_markup=keyb)
    elif msg.text.lower() == '😘 докажи 😘':
        randomstick = random.randint(0, 10)
        pic = stickers[randomstick]
        bot.reply_to(msg, "Создатель просил передать...", reply_markup=keyb)
        bot.send_sticker(msg.chat.id, pic)
    elif msg.text.lower() == '😞 грустно 😞':
        pic=open('s1200.jpeg', 'rb')
        bot.send_photo(msg.chat.id, pic)
        bot.reply_to(msg, "Ни грустииии", reply_markup=keyb)
    elif msg.text.lower() == '🤷‍♂️ нипанятнаа 🤷‍♂️':
        bot.reply_to(msg, """Если хочешь узнать тайну 
нажми ❤️ Секрет ❤️ 
Если нужны доказательства 
нажми 😘 Докажи 😘 
Если грустно 
нажми 😞 Грустно 😞 
Если ничего не понятно
нажми 🤷‍♂️ Нипанятнаа 🤷‍♂️""", reply_markup=keyb)
    elif msg.text.lower() == 'а я котю люблю':
        bot.reply_to(msg, "Создатель это знает. Именно поэтому он меня создал")
        bot.send_message(msg.chat.id, "❤️")


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route('/', methods=["GET"])
def index():
    return "Hello from Heroku!", 200


if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url=f'{URLHEROKU}' + TOKEN)
    print(bot.get_webhook_info().__dict__)
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

    # bot.polling(none_stop=True)
