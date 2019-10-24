from config import TOKEN
import telebot
import os
from flask import Flask, request
from config import *
 
 
 
 
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)
 
 
 
@bot.message_handler(commands=['start'])
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
    bot.remove_webhook()
    bot.set_webhook(url=f'{URLHEROKU}' + TOKEN)
    print(bot.get_webhook_info().__dict__)
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
    #bot.polling(none_stop=True)
