import os
import datetime
from datetime import datetime, date, time
import re
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

day = '''☀️День.
Самое время пофармить мобов и заработать денег на патроны'''

night = '''🌑Ночь.
Самое время убить кого-то из игроков и повысить свой ⚜️Ранг'''

zeros = "00.00.00"
threeam = "03.00.00"
sixam = "06.00.00"
nineam = "09.00.00"
twelwe = "12.00.00"
threepm = "15.00.00"
sixpm = "18.00.00"
ninepm = "21.00.00"
@bot.message_handler(commands=['daytime'])
def faza(msg):
    systime = datetime.now()
    if threepm < systime.strftime("%H.%M.%S") > sixpm:
        countfaza = threeam - systime.strftime("%H.%M.%S")
        print(countfaza)
        print(systime.strftime("%H.%M.%S"))
    
    if 6<= int(systime.strftime("%H")) < 9 or 12 <= int(systime.strftime("%H")) < 15 or 18 <= int(systime.strftime("%H")) < 21:
        daypart = day
    else:
        daypart = night
    bot.send_message(msg.chat.id, f'''Текущее время суток - {daypart}
До смены времени суток осталось - 
До выброса осталось - ''')

@bot.message_handler(content_types=['text'])
def frwrdmess(msg):
    if msg.forward_from != None:
        if msg.forward_from.id == 738720259:
            if '🔪Части мутантов' in msg.text:
                messtext = msg.text.strip('''\n''')
                if messtext.find('''Хвост 🐶Собаки''') != -1:
                    dog_tail_q = float(re.search(r'''Хвост 🐶Собаки\s(\d+)\sшт''' , messtext).group(1))
                else:
                    dog_tail_q = 0.0
                if messtext.find('''Рука 🧟‍♂️Зомби''') != -1:
                    zombie_hand_q = float(re.search(r'''Рука 🧟‍♂️Зомби\s(\d+)\sшт''' , messtext).group(1))
                else:
                    zombie_hand_q = 0.0
                if messtext.find('''Копыто 🐗Кабана''') != -1:
                    hog_hoof_q = float(re.search(r'''Копыто 🐗Кабана\s(\d+)\sшт''' , messtext).group(1))
                else:
                    hog_hoof_q = 0.0
                if messtext.find('''Нога 🦑Кровососа''') != -1:
                    sucker_leg_q = float(re.search(r'''Нога 🦑Кровососа\s(\d+)\sшт''' , messtext).group(1))
                else:
                    sucker_leg_q = 0.0
                if messtext.find('''Стопа 🦐Снорка''') != -1:
                    snork_foot_q = float(re.search(r'''Стопа 🦐Снорка\s(\d+)\sшт''' , messtext).group(1))
                else:
                    snork_foot_q = 0.0
                if messtext.find('''Голова 🐀Тушканчика''') != -1:
                    jerboa_head_q = float(re.search(r'''Голова 🐀Тушканчика\s(\d+)\sшт''' , messtext).group(1))
                else:
                    jerboa_head_q = 0.0
                if messtext.find('''Голова 🦐Снорка''') != -1:
                    snork_head_q = float(re.search(r'''Голова 🦐Снорка\s(\d+)\sшт''' , messtext).group(1))
                else:
                    snork_head_q = 0.0
                if messtext.find('''Нога 🐸Бюрера''') != -1:
                    burer_leg_q = float(re.search(r'''Нога 🐸Бюрера\s(\d+)\sшт''' , messtext).group(1))
                else:
                    burer_leg_q = 0.0
                if messtext.find('''Рука 👮‍♂️Контролёра''') != -1:
                    controler_hand_q = float(re.search(r'''Рука 👮‍♂️Контролёра\s(\d+)\sшт''' , messtext).group(1))
                else:
                    controler_hand_q = 0.0
                if messtext.find('''Рука 🐸Бюрера''') != -1:
                    burer_hand_q = float(re.search(r'''Рука 🐸Бюрера\s(\d+)\sшт''' , messtext).group(1))
                else:
                    burer_hand_q = 0.0
                if messtext.find('''Щупальца 🦑Кровососа''') != -1:
                    sucker_tentacle_q = float(re.search(r'''Щупальца 🦑Кровососа\s(\d+)\sшт''' , messtext).group(1))
                else:
                    sucker_tentacle_q = 0.0
                if messtext.find('''Нога 🐘Псевдогиганта''') != -1:
                    pseudo_giant_q = float(re.search(r'''Нога 🐘Псевдогиганта\s(\d+)\sшт''' , messtext).group(1))
                else:
                    pseudo_giant_q = 0.0
                if messtext.find('''Мозг 👮‍♂️Контролёра''') != -1:
                    controler_brain_q = float(re.search(r'''Мозг 👮‍♂️Контролёра\s(\d+)\sшт''' , messtext).group(1))
                else:
                    controler_brain_q = 0.0               
                if messtext.find('''Коготь 🐶🐈Химеры''') != -1:
                    chimera_claw_q = float(re.search(r'''Коготь 🐶🐈Химеры\s(\d+)\sшт''' , messtext).group(1))
                else:
                    chimera_claw_q = 0.0
                if messtext.find('''Сердце 🔥Полтергейста''') != -1:
                    poltergeist_heart_q = float(re.search(r'''Сердце 🔥Полтергейста\s(\d+)\sшт''' , messtext).group(1))
                else:
                    poltergeist_heart_q = 0.0
                gesheft = (dog_tail_q * 50.0) + (zombie_hand_q * 62.5) + (hog_hoof_q * 100.0) + (sucker_leg_q * 125.0) + (snork_foot_q * 150.0) + (jerboa_head_q * 166.5) + (snork_head_q * 200.0) + (burer_leg_q * 375.0) + (controler_hand_q * 625.0) + (burer_hand_q * 625.0) + (sucker_tentacle_q * 750.0) + (pseudo_giant_q * 750) + ( controler_brain_q * 1250) + (chimera_claw_q * 1250) + (poltergeist_heart_q * 1875.0)
                gesheft_science = gesheft * 4
                gesheft_premium_a = gesheft * 1.1
                gesheft_premium_b = gesheft * 1.25
                gesheft_premium_c = gesheft * 1.45
                gesheft_science_premium_a = gesheft_science * 1.1
                gesheft_science_premium_b = gesheft_science * 1.25
                gesheft_science_premium_c = gesheft_science * 1.45
                bot.send_message(msg.chat.id, f'''Выручка от продажи частей мутантов составит:
                
если продавать торговцу
{int(gesheft)}💰 без премиум аккаунта
{int(gesheft_premium_a)}💰 с премиум статусом α
{int(gesheft_premium_b)}💰 с премиум статусом β
{int(gesheft_premium_c)}💰 с премиум статусом γ

если продавать ученым
{int(gesheft_science)}💰 без премиум аккаунта
{int(gesheft_science_premium_a)}💰 с премиум статусом α
{int(gesheft_science_premium_b)}💰 с премиум статусом β
{int(gesheft_science_premium_c)}💰 с премиум статусом γ

Удачи, сталкер''')
            else:
                bot.send_message(msg.chat.id, '''Разве это инвентарь?''')
        else:
            bot.send_message(msg.chat.id, '''Странный форвард, нет?''') 
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
