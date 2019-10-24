from config import TOKEN
import telebot
from telebot import types
import random
TOKEN = '971858815:AAGd5HKRgTmUFpaxo4S4szOmonfA0T0EZqI'
import os
from flask import Flask, request
from config import *




bot = telebot.TeleBot(TOKEN)

markup = types.ReplyKeyboardMarkup(True, False)
markup.row(('Секрет', 'Доказательство', 'Грустно')
markup.row('Памагити')

#stickers for random
stickers = ["CAADAgADCwADlp-MDpuVH3sws_a7FgQ", "CAADAgAD7g0AAqgILwj_8DhBu2dnDRYE", "CAADBAADfQADzjkIDSgZQLclD7jiFgQ", "CAADBAADRAADzjkIDbv4-ULKD6hiFgQ", "CAADAgAD0gIAArnzlwt4AXAE0tVijhYE", "CAADAgAD2gEAAsdjXBUX3pc5V_GYDBYE", "CAADBAADmAADzjkIDRaa2RCZbCJWFgQ", "CAADBAADkwADzjkIDYydFNXPYxHoFgQ", "CAADAgAD4w0AAqgILwh6UH_uBQWn_RYE", "CAADAgADBAgAAhhC7ghzMDDTpZ3HjRYE", "CAADAgADCAADl_TGFHTucAABYtoR1BYE"]

server = Flask(__name__)



@bot.message_handler(commands=['start'])
def start(message):
    bot.sendMessage(chat_id=message.chat_id, text="Привет, если хочешь узнать тайну, Нажми Секрет. Если нужны доказательства - нажми Доказательство. Если грустно - нажми Грустно. Если нужна помощь - нажми Памагити")	
    bot.register_next_step_handler(message, menu)
@bot.message_handler(content_types=['text'])
def menu(message: types.Message):
    if message.text.lower() == 'секрет':
        bot.sendMessage(chat_id=message.chat_id, text="Мой создатель любит Лапу", reply_markup=markup)
    if message.text.lower() == 'памагити':
        bot.sendMessage(chat_id=message.chat_id, text="если хочешь узнать тайну, Нажми Секрет. Если нужны доказательства - нажми Доказательство. Если грустно - нажми Грустною Если нужна помощь - нажми Памагити", reply_markup=markup)
    if message.text.lower() == 'доказательство':
        randomstick=random.randint(0,10)
        pic=stickers[randomstick]
        bot.sendSticker(chat_id=message.chat_id, sticker=pic, reply_markup=markup)
    if message.text.lower() == 'грустно':
        pic=open('s1200.jpeg', 'rb')
        bot.send_photo(chat_id=message.chat_id, photo=pic)
        bot.sendMessage(chat_id=message.chat_id, text="Ни грустииии", reply_markup=markup)

def start_message(msg):
    bot.send_message(msg.chat.id, f'Даров {msg.from_user.first_name}')


@bot.message_handler(func=lambda m: True)
def echo_all(msg):
    bot.reply_to(msg, msg.text)






@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route('/', methods=["GET"])
def index():
    return "Hello from Heroku!", 200


if __name__ == '__main__':
     bot.polling(none_stop=True)
    bot.remove_webhook()
    bot.set_webhook(url=f'{URLHEROKU}' + TOKEN)
    print(bot.get_webhook_info().__dict__)
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
    #bot.polling(none_stop=True)
