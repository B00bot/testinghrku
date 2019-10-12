# coding=utf-8
import telebot
from telebot import types
import random

TOKEN = '971858815:AAGd5HKRgTmUFpaxo4S4szOmonfA0T0EZqI'

bot = telebot.TeleBot(TOKEN)
stick1="CAADAgADCwADlp-MDpuVH3sws_a7FgQ"
stick2="CAADAgAD7g0AAqgILwj_8DhBu2dnDRYE"
stick3="CAADBAADfQADzjkIDSgZQLclD7jiFgQ"
stick4="CAADBAADRAADzjkIDbv4-ULKD6hiFgQ"
stick5="CAADAgAD0gIAArnzlwt4AXAE0tVijhYE"

@bot.message_handler(commands=['start'])
def startpg(message):
    startmenu = types.ReplyKeyboardMarkup(True, False)
    startmenu.row('Секрет', 'Доказательство')
    startmenu.row('Грустно')
    startmenu.row('Нипанятнаа')
    bot.send_message(message.chat.id, 'Привет. Если хочешь узнать секрет, нажми секрет. Если нужно доказательство, нажми Доказательство. Если грустно, нажми Грустно. Если нужна помошь - нажми Нипанятнаа', reply_markup=startmenu)
    
@bot.message_handler(content_types=['text'])
def msg(message):
    if message.text == 'Секрет':
        bot.send_message(message.chat.id, "Мой создатель любит Лапу")
    elif message.text == 'Доказательство':
        def proof():
            randomstick=random.randint(1,5)
            if randomstick==1:
                pic=stick1
            elif randomstick==2:
                pic=stick2
            elif randomstick==3:
                pic=stick3
            elif randomstick==4:
                pic=stick4
            elif randomstick==5:
                pic=stick5
            bot.sendSticker(message.chat_id, sticker=pic) 
    elif message.text == 'Грустно':
        def grustno():
            pic=open('s1200.jpeg', 'rb')
            bot.send_photo(message.chat_id, photo=pic);
            bot.sendMessage(message.chat_id, "Ни грустииии") 
    elif message.text == 'Нипанятнаа':
        bot.send_message(message.chat.id, 'Если хочешь узнать секрет, нажми секрет. Если нужно доказательство, нажми Доказательство. Если грустно, нажми Грустно.')

bot.polling(none_stop=True)
    
