import telebot
from telebot import types
import load_bd
import requests
import exel
requests.packages.urllib3.disable_warnings()
token = ''

bot = telebot.TeleBot(token)



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Введите название задачи')
    bot.register_next_step_handler(message, handle)
    print(message.chat.id)

def handle(message):
    global org
    org = message.text
    bot.send_message(message.chat.id, 'Введите имя, фамилию исполнителя')
    bot.register_next_step_handler(message, data)

def data(message):
    global name
    name = message.text
    bot.send_message(message.chat.id, 'Введите срок исполнения')
    bot.register_next_step_handler(message, rab)

def rab(message):
    global date
    date = message.text
    bot.send_message(message.chat.id, 'Введите описание задачи')
    bot.register_next_step_handler(message, it)

def it(message):
    global name, org, date, locac, work
    locac = message.text
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Отправить", callback_data="Otpr")
    button2 = types.InlineKeyboardButton("Заново", callback_data="Zan")
    markup.add(button1, button2)
    bot.send_message(message.chat.id, "Запись готова")
    bot.send_message(message.chat.id, f"Исполнитель - {name}\n Название задачи - {org} \nСрок исполнения - {date}\nОписание задачи - {locac}",reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "Otpr")
def itog(call):
    if call.data == "Otpr":
        global name, org, date, locac
        bot.send_message(call.message.chat.id,"Отправлено!",reply_markup=types.ReplyKeyboardRemove())
        load_bd.load(name, org, date, locac)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        exel.all_B(bot,481776488)
        start(call.message)
        
        

@bot.callback_query_handler(func=lambda call: call.data == "Zan")
def zan(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)
    start(call.message)


bot.infinity_polling()