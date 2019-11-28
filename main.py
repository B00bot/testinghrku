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
перешли мне сообщение с инвентарем и я посчитаю тебе выручку от продажи частей мутантов.''')

#Объявляем переменные со стоимостью частей мутантов

dog_tail=50
zombie_hand=62.5
hog_hoof=100
sucker_leg=125
snork_foot=150
jerboa_head=166.5
snork_head=200
burer_leg=375
controler_hand=625
burer_hand=625
sucker_tentacle=750
pseudo_giant=750
controler_brain=1250
chimera_claw=1250
poltergeist_heart=1875


@bot.message_handler(content_types=['text'])
def frwrdmess(msg):
    if msg.forward_from != None:
        if msg.forward_from.id == 738720259:
            if '🔪Части мутантов' in msg.text:
                messtext = msg.text.strip('''\n''')
                bot.send_message(msg.chat.id, '''Схоронил''')
                print(messtext)
                dog_tail_q = messtext.find('''Хвост 🐶Собаки''') + 14
                print(dog_tail_q)
                print(messtext[dog_tail_q])
            else:
                bot.send_message(msg.chat.id, '''Разве это инвентарь?''')
        else:
            bot.send_message(msg.chat.id, '''Странный форвард, нет?''') 
            fromid = msg.forward_from.id
            print(fromid)
    else:
        bot.send_message(msg.chat.id, '''Не форвард''')

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
