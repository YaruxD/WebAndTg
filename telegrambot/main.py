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
    
    #Добавление в базу данных
    cursor.execute('SELECT * FROM telegram_users WHERE username = ?', (message.from_user.username,))
    telegram_user = cursor.fetchone()
    if telegram_user is None:
        cursor.execute('INSERT INTO telegram_users(username) VALUES (?)', (message.from_user.username,))
        connection.commit()
#Функции

#Каталог
def catalog(call):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Кроссовки', callback_data='Sneakers')
    button2 = types.InlineKeyboardButton('Верхняя одежда', callback_data='Outwear')
    button3 = types.InlineKeyboardButton('Джинсы', callback_data='Jeans')

    button4 = types.InlineKeyboardButton('Корзина', callback_data='shoppingcart')
    button5 = types.InlineKeyboardButton('Меню', callback_data='menu')

    markup.row(button1, button2, button3)
    markup.row(button4)
    markup.row(button5)

    bot.send_message(call.message.chat.id, "Выберете тип товара", reply_markup=markup)
    bot.answer_callback_query(call.id)
    
    

#Покупка
def buy_function(call):
    bot.send_message(call.message.chat.id, "Buy function is called!")
    bot.answer_callback_query(call.id)

 #Помощь   
def help_function(call):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton('Меню', callback_data='menu')
    markup.row(btn)
    bot.send_photo(call.message.chat.id, photo = "https://yandex-images.clstorage.net/5Qc1GL213/4fbe6a5Cotzx/Ox6La7YlLU6KzJ3zggFcA6lTt-ianlzs_5jGQ-l4-j19liHuP86WHPgeI-dglyQ-MI9NuzA0Ejtk1T8-Y8fY1E8Lz15SVS0fznw5MiLAXVdoh4a8uw4cmW9YxfVO6o2b6iAzacjcEomt63Yj8UOVfaZOf9zVchV5swZPOabxbXAJ3Ttocub8rh1cnJOxQ332GSG372urbD3KHqb3PnrNejuQsSrpDBAaz4pl01Ux9o4ki0ye5kNnSJFW76pVMp9x2CzKWLPFrz0urk6wU8MelgqhZ51Leq09K81Gl935rUr5keNJOK5Biuyp92EVMSZfdzg87qZgdKujBC7a52Hs0orfihmzZ63ejM1885ARH1foI9XOqlg_LhiPBCQsaz2o-FPBWSpuYQnvKhSiF0B0PHXInp8VE4QYcaedivdAboFobTsIkud8r59uLvOzI7yFCCMnzPqZD1x6zTY2zbo9OtmwMrl4vBBrDKgG4gVgdD432Ly_liPHWXEXj7m0wFzhOiyqyeD1bR0OHX3xEJJO5gsQxy46Kt9emc0GpazYLYi6w0PZ-F9gK13YN3JVQNV-RTl-zlRAdWuxBLyIBRBcw8s96KmhZF_9nayuoPICbIbIEGTMSKlc_9rcVMe8uM-qWBFz6Qveg_mNe3Zil3GmfqeL_y21EIaJkWZtqFbzj9N4bGr4kOSMTj0vbWHCkcwES3M1PIjY7_-a3PSnvAkcGFnzwrt5XiO67aqmUGcgBO4Fq_18Z8HFy-NHXKqGgP2xuUwLOjIlPZ-vf4xCQtFsFaszJ_7LeQ9fqL2lF-4IvJppsEMZ-ewBKO07FMIlIOc_RMivPxQCRqqTp9_Yd9J803tMucvz50_N3W18kQHh3qd4kaSOWTucDOiPdHXtqh1bGiGDqcrd8VtPafSQh1IljsaI_24HcgeKA2RPSdQibdKpHbh6I4Sdb3493NFyoB-32sKFvospnyzI3KVEk", caption = "Help function!", reply_markup=markup)
    bot.answer_callback_query(call.id)

#Меню
def menu(call):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Каталог', callback_data='catalog')
    button2 = types.InlineKeyboardButton('Buy', callback_data='buy')
    button3 = types.InlineKeyboardButton('Help', callback_data='help')
    markup.row(button1, button2, button3)
    bot.send_photo(call.message.chat.id, photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwnfyzqed8Y9tb31w1c1WdQ2AB3zKPOhMccNFliydz5GPEUqGGzz42VlBKAdIj93jR4bc&usqp=CAU', caption="Welcome to the shop!", reply_markup=markup)
    bot.answer_callback_query(call.id)

#Корзина
def shoppingcart(call):
    bot.send_message(call.message.chat.id, call.message.caption)
    bot.answer_callback_query(call.id)

#Лист товаров
def ProductSheet(call):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Меню', callback_data='menu')
    btn2 = types.InlineKeyboardButton('Добавить в корзину', callback_data='shoppingcart')
    markup.row(btn1)
    markup.row(btn2)
    
    cursor.execute(f'SELECT * FROM catalog WHERE Type = "{call.data}";')
    data = cursor.fetchall()
    
    #print(data)

    for i in range(len(data)):
        
        bot.send_photo(call.message.chat.id, photo=data[i][4], caption=f'{data[i][2]} \n{data[i][3]}', reply_markup=markup)

    bot.answer_callback_query(call.id)
    


callback_map = {
    'catalog': catalog,
    'buy': buy_function,
    'help': help_function,
    'menu': menu,
    'shoppingcart': shoppingcart,
    'Sneakers': ProductSheet,
    'Outwear': ProductSheet,
    'Jeans': ProductSheet,
}

bot.polling(none_stop=True)