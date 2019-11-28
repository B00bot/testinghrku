import os

import telebot
from telebot import types
from config import *
from config import TOKEN
from flask import Flask, request

bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def start_message(msg):
    bot.send_message(msg.chat.id, f'''Привет, {msg.from_user.first_name}, 
перешли мне сообщение с инвентарем и я посчитаю тебе выручку от продажи частей мутантов.'''

#################
#Объявляем переменные со стоимостью частей мутантов
#################
int dogtail = 50
int zombiehand = 62.5
int hoghoof = 100
int suckerleg = 125
int snorkfoot = 150
int jerboahead = 166.5
int snorkhead = 200
int burerleg = 375
int controlerhand = 625
int burerhand = 625
int suckertentacle = 750
int pseudogiant = 750
int controlerbrain = 1250
int chimeraclaw = 1250
int poltergeistheart = 1875
#######################

@bot.message_handler(content_types=['text'])
def frwrdmess(msg)
if message.forward_from != None:
    if message.forward_from == "738720259":
        messtext = msg.text.strip(“\n”)
        bot.send_message(msg.chat.id, '''Схоронил'''
    else:
        bot.send_message(msg.chat.id, '''Странный форвард, нет?'''   


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
