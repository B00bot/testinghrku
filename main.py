import os
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

#Объявляем переменные со стоимостью частей мутантов

dog_tail=50.0
zombie_hand=62.5
hog_hoof=100.0
sucker_leg=125.0
snork_foot=150.0
jerboa_head=166.5
snork_head=200.0
burer_leg=375.0
controler_hand=625.0
burer_hand=625.0
sucker_tentacle=750.0
pseudo_giant=750.0
controler_brain=1250.0
chimera_claw=1250.0
poltergeist_heart=1875.0


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
                print(dog_tail_q)
                if messtext.find('''Рука 🧟‍♂️Зомби''') != -1:
                    zombie_hand_q = float(re.search(r'''Рука 🧟‍♂️Зомби\s(\d+)\sшт''' , messtext).group(1))
                else:
                    zombie_hand_q = 0.0
                print(zombie_hand_q)
                if messtext.find('''Копыто 🐗Кабана''') != -1:
                    hog_hoof_q = float(re.search(r'''Копыто 🐗Кабана\s(\d+)\sшт''' , messtext).group(1))
                else:
                    hog_hoof_q = 0.0
                print(hog_hoof_q)
                if messtext.find('''Нога 🦑Кровососа''') != -1:
                    sucker_leg_q = float(re.search(r'''Нога 🦑Кровососа\s(\d+)\sшт''' , messtext).group(1))
                else:
                    sucker_leg_q = 0.0
                print(sucker_leg_q)
                if messtext.find('''Стопа 🦐Снорка''') != -1:
                    snork_foot_q = float(re.search(r'''Стопа 🦐Снорка\s(\d+)\sшт''' , messtext).group(1))
                else:
                    snork_foot_q = 0.0
                print(snork_foot_q)
                if messtext.find('''Голова 🐀Тушканчика''') != -1:
                    jerboa_head_q = float(re.search(r'''Голова 🐀Тушканчика\s(\d+)\sшт''' , messtext).group(1))
                else:
                    jerboa_head_q = 0.0
                print(jerboa_head_q)
                if messtext.find('''Голова 🦐Снорка''') != -1:
                    snork_head_q = float(re.search(r'''Голова 🦐Снорка\s(\d+)\sшт''' , messtext).group(1))
                else:
                    snork_head_q = 0.0
                print(snork_head_q)
                if messtext.find('''Нога 🐸Бюрера''') != -1:
                    burer_leg_q = float(re.search(r'''Нога 🐸Бюрера\s(\d+)\sшт''' , messtext).group(1))
                else:
                    burer_leg_q = 0.0
                print(burer_leg_q)
                if messtext.find('''Рука 👮‍♂️Контролёра''') != -1:
                    controler_hand_q = float(re.search(r'''Рука 👮‍♂️Контролёра\s(\d+)\sшт''' , messtext).group(1))
                else:
                    controler_hand_q = 0.0
                print(controler_hand_q)
                if messtext.find('''Рука 🐸Бюрера''') != -1:
                    burer_hand_q = float(re.search(r'''Рука 🐸Бюрера\s(\d+)\sшт''' , messtext).group(1))
                else:
                    burer_hand_q = 0.0
                print(burer_hand_q)
                if messtext.find('''Щупальца 🦑Кровососа''') != -1:
                    sucker_tentacle_q = float(re.search(r'''Щупальца 🦑Кровососа\s(\d+)\sшт''' , messtext).group(1))
                else:
                    sucker_tentacle_q = 0.0
                print(sucker_tentacle_q)
                if messtext.find('''Нога 🐘Псевдогиганта''') != -1:
                    pseudo_giant_q = float(re.search(r'''Нога 🐘Псевдогиганта\s(\d+)\sшт''' , messtext).group(1))
                else:
                    pseudo_giant_q = 0.0
                print(pseudo_giant_q)
                if messtext.find('''Мозг 👮‍♂️Контролёра''') != -1:
                    controler_brain_q = float(re.search(r'''Мозг 👮‍♂️Контролёра\s(\d+)\sшт''' , messtext).group(1))
                else:
                    controler_brain_q = 0.0
                print(controler_brain_q)
                if messtext.find('''Коготь 🐶🐈Химеры''') != -1:
                    chimera_claw_q = float(re.search(r'''Коготь 🐶🐈Химеры\s(\d+)\sшт''' , messtext).group(1))
                else:
                    chimera_claw_q = 0.0
                if messtext.find('''Сердце 🔥Полтергейста''') != -1:
                    poltergeist_heart_q = float(re.search(r'''Сердце 🔥Полтергейста\s(\d+)\sшт''' , messtext).group(1))
                else:
                    poltergeist_heart_q = 0.
                gesheft = (dog_tail_q * dog_tail) + (zombie_hand_q * zombie_hand) + (hog_hoof_q * hog_hoof) + (sucker_leg_q * sucker_leg) + (snork_foot_q * snork_foot) + (jerboa_head_q * jerboa_head) + (snork_head_q * snork_head) + (burer_leg_q * burer_leg) + (controler_hand_q * controler_hand) + (burer_hand * burer_hand_q) + (sucker_tentacle_q * sucker_tentacle_q) + (pseudo_giant_q * pseudo_giant) + ( controler_brain_q * controler_brain) + (chimera_claw_q * chimera_claw) + (poltergeist_heart_q * poltergeist_heart)
                gesheft_science = gesheft * 4
                bot.send_message(msg.chat.id, f'''Выручка от продажи частей мутантов составит:
{int(gesheft)}💰 - если продавать торговцу.
{int(gesheft_science)}💰 - если продавать ученым.

Удачи, сталкер''')
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
