import telebot
from telebot import types

import sqlite3
connection = sqlite3.connect('C:/WebAndTg/WebSite/backend/db.sqlite3', check_same_thread=False)
cursor = connection.cursor()



bot = telebot.TeleBot('7648629772:AAHB6GsiB_V9o98zmazwvUWI-h_lxLYY5ns')

#Перенаправление колбеков в callback_map
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data in callback_map:
        callback_map[call.data](call)  

#Приглашение
@bot.message_handler(commands=['start'])
def welcompage(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Каталог', callback_data='catalog')
    button2 = types.InlineKeyboardButton('Buy', callback_data='buy')
    button3 = types.InlineKeyboardButton('Help', callback_data='help')
    markup.row(button1, button2, button3)
    bot.send_photo(message.chat.id, photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwnfyzqed8Y9tb31w1c1WdQ2AB3zKPOhMccNFliydz5GPEUqGGzz42VlBKAdIj93jR4bc&usqp=CAU', caption="Welcome to the shop!", reply_markup=markup)
    cursor.execute('INSERT INTO telegram_users(username) values(?)', [message.from_user.username])
    connection.commit()

#Функции

#Каталог
def catalog(call):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Кроссовки', callback_data='sneakers')
    button2 = types.InlineKeyboardButton('Верхняя одежда', callback_data='outerwear')
    button3 = types.InlineKeyboardButton('Джинсы', callback_data='jeans')
    button4 = types.InlineKeyboardButton('Корзина', callback_data='shoppingcart')
    button5 = types.InlineKeyboardButton('Меню', callback_data='menu')

    markup.row(button1, button2, button3)
    markup.row(button4)
    markup.row(button5)

    bot.send_message(call.message.chat.id, "Выберете тип товара", reply_markup=markup)
    bot.answer_callback_query(call.id)
    
    

def buy_function(call):
    bot.send_message(call.message.chat.id, "Buy function is called!")
    bot.answer_callback_query(call.id)
    
def help_function(call):
    bot.send_message(call.message.chat.id, "Help function is called!")
    bot.answer_callback_query(call.id)

def menu(call):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Каталог', callback_data='catalog')
    button2 = types.InlineKeyboardButton('Buy', callback_data='buy')
    button3 = types.InlineKeyboardButton('Help', callback_data='help')
    markup.row(button1, button2, button3)
    bot.send_photo(call.message.chat.id, photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwnfyzqed8Y9tb31w1c1WdQ2AB3zKPOhMccNFliydz5GPEUqGGzz42VlBKAdIj93jR4bc&usqp=CAU', caption="Welcome to the shop!", reply_markup=markup)
    bot.answer_callback_query(call.id)

def shoppingcart(call):
    pass


callback_map = {
    'catalog': catalog,
    'buy': buy_function,
    'help': help_function,
    'menu': menu,
    'shoppingcart': shoppingcart,
}

bot.polling(none_stop=True)