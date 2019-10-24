import os

import telebot
from config import *
from config import TOKEN
from flask import Flask, request
import random

bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

stickers = ["CAADAgADCwADlp-MDpuVH3sws_a7FgQ", "CAADAgAD7g0AAqgILwj_8DhBu2dnDRYE", "CAADBAADfQADzjkIDSgZQLclD7jiFgQ", "CAADBAADRAADzjkIDbv4-ULKD6hiFgQ", "CAADAgAD0gIAArnzlwt4AXAE0tVijhYE", "CAADAgAD2gEAAsdjXBUX3pc5V_GYDBYE", "CAADBAADmAADzjkIDRaa2RCZbCJWFgQ", "CAADBAADkwADzjkIDYydFNXPYxHoFgQ", "CAADAgAD4w0AAqgILwh6UH_uBQWn_RYE", "CAADAgADBAgAAhhC7ghzMDDTpZ3HjRYE", "CAADAgADCAADl_TGFHTucAABYtoR1BYE"]


@bot.message_handler(commands=['start'])
def start_message(msg):
    bot.send_message(msg.chat.id, "Привет, если хочешь узнать тайну, отправь /secret Если нужны доказательства - отправь /proof Если грустно - отправь /grustno")


@bot.message_handler(commands=['secret'])
def secret_message(msg):
    bot.send_message(msg.chat.id, "Мой создатель любит тебя")

@bot.message_handler(commands=['help'])
def help_message(msg):
    bot.send_message(msg.chat.id, "Если хочешь узнать тайну, отправь /secret Если нужны доказательства - отправь /proof Если грустно - отправь /grustno")

@bot.message_handler(commands=['proof'])
def proof_message(msg):
    randomstick = random.randint(0, 10)
    pic = stickers[randomstick]
    bot.send_message(msg.chat.id, "Создатель просил передать...")
    bot.send_sticker(msg.chat.id, pic);

@bot.message_handler(commands=['grustno'])
def grustno(msg):
    pic=open('s1200.jpeg', 'rb')
    bot.send_photo(msg.chat.id, pic);
    bot.send_message(msg.chat.id, "Ни грустииии")

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


