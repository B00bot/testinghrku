import os

import telebot
from telebot import types
from config import *
from config import TOKEN
from flask import Flask, request
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Boolean, MetaData, Table
from sqlalchemy.orm import mapper, sessionmaker
from model import *
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def start_message(msg):
    bot.send_message(msg.chat.id, f'''Привет, {msg.from_user.first_name}, 
перешли мне сообщение с инвентарем и я посчитаю тебе выручку от продажи частей мутантов.'''

@bot.message_handler(content_types=['text'])
def parse_msg(msg):
    if 'Части мутантов'in msg.text:
        try:
            if msg.forward_from.id == 738720259:
                parse_imventory(msg)
                if str(msg.chat.id)[0] == '-':
                    bot.reply_to(msg, f'Cпасибо за твой инвентарь {msg.from_user.first_name}')
        except:
            bot.send_message(msg.chat.id, 'Странный форвард, не находишь?')





 🔪

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route('/', methods=["GET"])
def index():
    return "5 минут, полет нормальный", 200

if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url=f'{URLHEROKU}' + TOKEN)
    print(bot.get_webhook_info().__dict__)
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
