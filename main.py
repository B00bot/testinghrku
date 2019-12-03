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

@bot.message_handler(commands=['daytime'])
def faza(msg):
    systime = datetime.now()
    if  0 <= int(systime.strftime("%H")) <3 or 6<= int(systime.strftime("%H")) < 9 or 12 <= int(systime.strftime("%H")) < 15 or 18 <= int(systime.strftime("%H")) < 21:
        daypart = night
    else:
        daypart = day
    if (59 - int(systime.strftime("%M"))) < 10:
        count_minutes =str(0) + str(59 - int(systime.strftime("%M")))
    else:
        count_minutes = 59 - int(systime.strftime("%M"))
    if (59 - int(systime.strftime("%S"))) < 10:
        count_seconds =str(0) + str(59 - int(systime.strftime("%S")))
    else:
        count_seconds = 59 - int(systime.strftime("%S"))
    if int(systime.strftime("%H")) < 3:
        count_hours = 2 - int(systime.strftime("%H"))
    elif 3 < int(systime.strftime("%H")) < 6:
        count_hours = 5 - int(systime.strftime("%H"))
    elif 6 < int(systime.strftime("%H")) < 9:
        count_hours = 8 - int(systime.strftime("%H"))
    elif 9 < int(systime.strftime("%H")) < 12:
        count_hours = 11 - int(systime.strftime("%H"))
    elif 12 < int(systime.strftime("%H")) < 15:
        count_hours = 14 - int(systime.strftime("%H"))
    elif 15 < int(systime.strftime("%H")) < 18:
        count_hours = 17 - int(systime.strftime("%H"))
    elif 18 < int(systime.strftime("%H")) < 21 :
        count_hours = 20 - int(systime.strftime("%H"))
    else:
        count_hours = 23 - int(systime.strftime("%H"))
    bot.send_message(msg.chat.id, f'''Текущее время суток - {daypart}
До смены времени суток осталось:
⏱️ {count_hours}ч.{count_minutes}м.{count_seconds}с.''')

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
                artefacts_q = 0.0
                if messtext.find('''«Пузырь»''') != -1:
                    artefacts = float(re.search(r'''«Пузырь»\s(\d+)\sшт''' , messtext).group(1))
                    artefacts_q += artefacts
                else:
                    artefacts_q += 0.0
                if messtext.find('''«Грави»''') != -1:
                    artefacts = float(re.search(r'''«Грави»\s(\d+)\sшт''' , messtext).group(1))
                    artefacts_q += artefacts
                else:
                    artefacts_q += 0.0
                if messtext.find('''«Ломоть мяса»''') != -1:
                    artefacts = float(re.search(r'''«Ломоть мяса»\s(\d+)\sшт''' , messtext).group(1))
                    artefacts_q += artefacts
                else:
                    artefacts_q += 0.0
                if messtext.find('''«Медуза»''') != -1:
                    artefacts = float(re.search(r'''«Медуза»\s(\d+)\sшт''' , messtext).group(1))
                    artefacts_q += artefacts
                else:
                    artefacts_q += 0.0
                if messtext.find('''«Пламя»''') != -1:
                    artefacts = float(re.search(r'''«Пламя»\s(\d+)\sшт''' , messtext).group(1))
                    artefacts_q += artefacts
                else:
                    artefacts_q += 0.0
                if messtext.find('''«Ночная звезда»''') != -1:
                    artefacts = float(re.search(r'''«Ночная звезда»\s(\d+)\sшт''' , messtext).group(1))
                    artefacts_q += artefacts
                else:
                    artefacts_q += 0.0
                if messtext.find('''«Бенгальский огонь»''') != -1:
                    artefacts = float(re.search(r'''«Бенгальский огонь»\s(\d+)\sшт''' , messtext).group(1))
                    artefacts_q += artefacts
                else:
                    artefacts_q += 0.0
                if messtext.find('''«Душа»''') != -1:
                    artefacts = float(re.search(r'''«Душа»\s(\d+)\sшт''' , messtext).group(1))
                    artefacts_q += artefacts
                else:
                    artefacts_q += 0.0
                if messtext.find('''«Снежинка»''') != -1:
                    artefacts = float(re.search(r'''«Снежинка»\s(\d+)\sшт''' , messtext).group(1))
                    artefacts_q += artefacts
                else:
                    artefacts_q += 0.0
                if messtext.find('''«Выверт»''') != -1:
                    artefacts = float(re.search(r'''«Выверт»\s(\d+)\sшт''' , messtext).group(1))
                    artefacts_q += artefacts
                else:
                    artefacts_q += 0.0
                if messtext.find('''«Кристалл»''') != -1:
                    artefacts = float(re.search(r'''«Кристалл»\s(\d+)\sшт''' , messtext).group(1))
                    artefacts_q += artefacts
                else:
                    artefacts_q += 0.0
                if messtext.find('''«Слизь»''') != -1:
                    artefacts = float(re.search(r'''«Слизь»\s(\d+)\sшт''' , messtext).group(1))
                    artefacts_q += artefacts
                else:
                    artefacts_q += 0.0
                if messtext.find('''«Мамины бусы»''') != -1:
                    artefacts = float(re.search(r'''«Мамины бусы»\s(\d+)\sшт''' , messtext).group(1))
                    artefacts_q += artefacts
                else:
                    artefacts_q += 0.0
                if messtext.find('''«Батарейка»''') != -1:
                    artefacts = float(re.search(r'''«Батарейка»\s(\d+)\sшт''' , messtext).group(1))
                    artefacts_q += artefacts
                else:
                    artefacts_q += 0.0
                if messtext.find('''«Пустышка»''') != -1:
                    artefacts = float(re.search(r'''«Пустышка»\s(\d+)\sшт''' , messtext).group(1))
                    artefacts_q += artefacts
                else:
                    artefacts_q += 0.0
                if messtext.find('''«Вспышка»''') != -1:
                    artefacts = float(re.search(r'''«Вспышка»\s(\d+)\sшт''' , messtext).group(1))
                    artefacts_q += artefacts
                else:
                    artefacts_q += 0.0
                if messtext.find('''«Капли»''') != -1:
                    artefacts = float(re.search(r'''«Капли»\s(\d+)\sшт''' , messtext).group(1))
                    artefacts_q += artefacts
                else:
                    artefacts_q += 0.0
                if messtext.find('''«Лунный свет»''') != -1:
                    artefacts = float(re.search(r'''«Лунный свет»\s(\d+)\sшт''' , messtext).group(1))
                    artefacts_q += artefacts
                else:
                    artefacts_q += 0.0
                if messtext.find('''«Огненный шар»''') != -1:
                    artefacts = float(re.search(r'''«Огненный шар»\s(\d+)\sшт''' , messtext).group(1))
                    artefacts_q += artefacts
                else:
                    artefacts_q += 0.0
                if messtext.find('''«Кровь камня»''') != -1:
                    artefacts = float(re.search(r'''«Кровь камня»\s(\d+)\sшт''' , messtext).group(1))
                    artefacts_q += artefacts
                else:
                    artefacts_q += 0.0
                if messtext.find('''«Золотая рыбка»''') != -1:
                    artefacts = float(re.search(r'''«Золотая рыбка»\s(\d+)\sшт''' , messtext).group(1))
                    artefacts_q += artefacts
                else:
                    artefacts_q += 0.0
                if messtext.find('''«Каменный цветок»''') != -1:
                    artefacts = float(re.search(r'''«Каменный цветок»\s(\d+)\sшт''' , messtext).group(1))
                    artefacts_q += artefacts
                else:
                    artefacts_q += 0.0
                if messtext.find('''«Слюда»''') != -1:
                    artefacts = float(re.search(r'''«Слюда»\s(\d+)\sшт''' , messtext).group(1))
                    artefacts_q += artefacts
                else:
                    artefacts_q += 0.0
                if messtext.find('''«Глаз»''') != -1:
                    artefacts = float(re.search(r'''«Глаз»\s(\d+)\sшт''' , messtext).group(1))
                    artefacts_q += artefacts
                else:
                    artefacts_q += 0.0
                if messtext.find('''«Слизняк»''') != -1:
                    artefacts = float(re.search(r'''«Слизняк»\s(\d+)\sшт''' , messtext).group(1))
                    artefacts_q += artefacts
                else:
                    artefacts_q += 0.0
                gesheft = (dog_tail_q * 50.0) + (zombie_hand_q * 62.5) + (hog_hoof_q * 100.0) + (sucker_leg_q * 125.0) + (snork_foot_q * 150.0) + (jerboa_head_q * 166.5) + (snork_head_q * 200.0) + (burer_leg_q * 375.0) + (controler_hand_q * 625.0) + (burer_hand_q * 625.0) + (sucker_tentacle_q * 750.0) + (pseudo_giant_q * 750) + ( controler_brain_q * 1250) + (chimera_claw_q * 1250) + (poltergeist_heart_q * 1875.0)
                gesheft_science = gesheft * 4
                gesheft_premium_a = gesheft * 1.1
                gesheft_premium_b = gesheft * 1.25
                gesheft_premium_c = gesheft * 1.45
                gesheft_science_premium_a = gesheft_science * 1.1
                gesheft_science_premium_b = gesheft_science * 1.25
                gesheft_science_premium_c = gesheft_science * 1.45
                a_gesheft = artefacts_q * 5000
                a_gesheft_premium_a = a_gesheft * 1.1
                a_gesheft_premium_b = a_gesheft * 1.25
                a_gesheft_premium_c = a_gesheft * 1.45
                sum_gesheft = a_gesheft + gesheft_science
                sum_gesheft_premium_a = sum_gesheft * 1.1
                sum_gesheft_premium_b = sum_gesheft * 1.25
                sum_gesheft_premium_c = sum_gesheft * 1.45
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

Прибыль от продажи артефактов составит:
{int(a_gesheft)}💰 без премиум аккаунта
{int(a_gesheft_premium_a)}💰 с премиум статусом α
{int(a_gesheft_premium_b)}💰 с премиум статусом β
{int(a_gesheft_premium_c)}💰 с премиум статусом γ

Суммарная прибыль составит:
{int(sum_gesheft)}💰 без премиум аккаунта
{int(sum_gesheft_premium_a)}💰 с премиум статусом α
{int(sum_gesheft_premium_b)}💰 с премиум статусом β
{int(sum_gesheft_premium_c)}💰 с премиум статусом γ

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

