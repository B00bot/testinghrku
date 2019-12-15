import os

import telebot
from telebot import types
from config import TOKEN, URLHEROKU
from flask import Flask, request
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Boolean, MetaData, Table
from sqlalchemy.orm import mapper, sessionmaker

bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def start_msg(msg):
    bot.send_message(msg.chat.id, f'''Приветствую тебя в карточной игре {Game_name}. Как нам тебя называть?''')
    bot.register_next_step_handler(msg, process_name_step)

def process_name_step(msg):
    name = msg.text
    bot.send_message(msg.chat.id, f'''Приятно познакомиться, {name}. Выбери пол героя: М - мужчина, Ж - женщина''')
    bot.register_next_step_handler(msg, sex_step)

def sex_step(msg):
    if msg.text.lower == 'М':
        sex = 'Мужчина'
    elif msg.text.lower == 'Ж':
        sex = 'Женщина'
    bot.send_message(msg.chat.id, f'''Регистрация завершена. Твой персонаж {name}, пол - {sex})'''


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route('/', methods=["GET"])
def index():
    return "Оно живое, живое!", 200


if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url=f'{URLHEROKU}' + TOKEN)
    print(bot.get_webhook_info().__dict__)
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
