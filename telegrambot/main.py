import telebot
from telebot import types
import sqlite3




bot = telebot.TeleBot('7648629772:AAHB6GsiB_V9o98zmazwvUWI-h_lxLYY5ns')

#Перенаправление колбеков в callback_map
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data in callback_map:
        callback_map[call.data](call)  

@bot.message_handler(commands=['start'])
def welcompage(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Каталог', callback_data='catalog')
    button3 = types.InlineKeyboardButton('Help', callback_data='help')
    markup.row(button1, button3)
    bot.send_photo(message.chat.id, photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwnfyzqed8Y9tb31w1c1WdQ2AB3zKPOhMccNFliydz5GPEUqGGzz42VlBKAdIj93jR4bc&usqp=CAU', caption="Welcome to the shop!", reply_markup=markup)
    
    #Добавление в базу данных
    connection = sqlite3.connect('C:/WebAndTg/WebSite/backend/db.sqlite3', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM telegram_users WHERE username = ?', (message.from_user.username,))
    telegram_user = cursor.fetchone()
    if telegram_user is None:
        cursor.execute('INSERT INTO telegram_users(username) VALUES (?)', (message.from_user.username,))
        connection.commit()
    cursor.close()
    connection.close()
#Функции

#Каталог
def catalog(call):
    bot.delete_message(call.message.chat.id, message_id = call.message.id)
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Кроссовки', callback_data='Sneakers')
    button2 = types.InlineKeyboardButton('Верхняя одежда', callback_data='Outwear')
    button3 = types.InlineKeyboardButton('Джинсы', callback_data='Jeans')
    button4 = types.InlineKeyboardButton('Корзина', callback_data='shoppingcart')
    button5 = types.InlineKeyboardButton('Купленные товары', callback_data='bought_product')


    markup.row(button1, button2, button3)
    markup.row(button4,button5)



    bot.send_message(call.message.chat.id, "Выберете тип товара", reply_markup=markup)
    bot.answer_callback_query(call.id)
    
#Каталог без удаления
def catalog_without_delete(call):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Кроссовки', callback_data='Sneakers')
    button2 = types.InlineKeyboardButton('Верхняя одежда', callback_data='Outwear')
    button3 = types.InlineKeyboardButton('Джинсы', callback_data='Jeans')

    button4 = types.InlineKeyboardButton('Корзина', callback_data='shoppingcart')
    button5 = types.InlineKeyboardButton('Купленные товары', callback_data='bought_product')


    markup.row(button1, button2, button3)
    markup.row(button4,button5)

    bot.send_message(call.message.chat.id, "Выберете тип товара", reply_markup=markup)
    bot.answer_callback_query(call.id)
    

#Покупка
def get_in_shoppingcart(call):
    connection = sqlite3.connect('C:/WebAndTg/WebSite/backend/db.sqlite3', check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM sales WHERE username =? AND product=?;', (call.message.chat.username,(call.message.caption).split(' ')[0]))
    sale = cursor.fetchall()
    if (sale == []):
        cursor.execute('INSERT INTO sales(username, product, state, amount) values(?,?,?,?)', [call.message.chat.username, (call.message.caption).split(' ')[0], 0, 1])
    elif (sale[-1][4]==1):
        cursor.execute('INSERT INTO sales(username, product, state, amount) values(?,?,?,?)', [call.message.chat.username, (call.message.caption).split(' ')[0], 0, 1])
    else:
        cursor.execute('UPDATE sales SET amount = amount + 1 WHERE username =? AND product =?', [call.message.chat.username, (call.message.caption).split(' ')[0]])
 
    connection.commit()
    cursor.close()
    connection.close()
    #print(call.message.chat.username)
    bot.answer_callback_query(call.id)
    

 #Помощь   
def help_function(call):
    bot.delete_message(call.message.chat.id, message_id = call.message.id)
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton('Кататалог', callback_data='catalog')
    markup.row(btn)
    bot.send_message(call.message.chat.id, 'There is nothing here', reply_markup=markup)
    bot.answer_callback_query(call.id)



#Корзина
def shoppingcart(call):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Удалить из корзины', callback_data='delete_from_shoppingcart')
    btn2 = types.InlineKeyboardButton('Купить', callback_data='buy')
    markup.row(btn1, btn2)
    connection = sqlite3.connect('C:/WebAndTg/WebSite/backend/db.sqlite3', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM sales WHERE state=0 AND username=?', [call.message.chat.username])
    data = cursor.fetchall()
    all_price = 0
    #print(data)
    if data!= []:
        bot.send_message(call.message.chat.id, '//Вы вызвали корзину//')
        bot.delete_message(call.message.chat.id, message_id = call.message.id)
    else:
        bot.send_message(call.message.chat.id, '//Корзина пуста//')
    for i in data:
        cursor.execute('SELECT * FROM catalog WHERE Model=?', [i[2]])
        data2 = cursor.fetchone()
        bot.send_photo(call.message.chat.id, photo = data2[4], caption = f'{i[3]}шт. {i[2]} - {data2[5]}$ (шт)' , reply_markup=markup)
        all_price += data2[5]*int(i[3])
    if data!=[]:
        markup = types.InlineKeyboardMarkup()
        btn3 = types.InlineKeyboardButton('Купить всё', callback_data='buy_all')
        btn4 = types.InlineKeyboardButton('Каталог', callback_data='catalog')
        markup.row(btn3)
        markup.row(btn4)
        bot.send_message(call.message.chat.id, f'Общая стоимость: {all_price}', reply_markup=markup)

        #print(data2[4])

    bot.answer_callback_query(call.id)
    #print(data)

#Удаление вещи из корзины
def delete_from_shoppingcart(call):
    bot.delete_message(call.message.chat.id, message_id = call.message.id)
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Удалить из корзины', callback_data='delete_from_shoppingcart')
    markup.row(btn1)
    connection = sqlite3.connect('C:/WebAndTg/WebSite/backend/db.sqlite3', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM sales WHERE state=0 AND username=? AND product=?', [call.message.chat.username, (call.message.caption).split(' ')[1]])
    data = cursor.fetchone()
    if data== None:
        pass
    elif data[3] < 2:
        cursor.execute('DELETE FROM sales WHERE username=? AND product=?', [call.message.chat.username, (call.message.caption).split(' ')[1]])
    else:
        cursor.execute('UPDATE sales SET amount = amount - 1 WHERE username=? AND product=?', [call.message.chat.username, (call.message.caption).split(' ')[1]])
        cursor.execute('SELECT * FROM sales WHERE state=0 AND username=? AND product=?', [call.message.chat.username, (call.message.caption).split(' ')[1]])
        data_for_residual = cursor.fetchone()
        cursor.execute('SELECT * FROM catalog WHERE Model=?', [(call.message.caption).split(' ')[1]])
        data_for_photo = cursor.fetchone()
        #print(data_for_photo)
        #print(data_for_residual)
        bot.send_photo(call.message.chat.id, photo = data_for_photo[4], caption=f'{data_for_residual[3]} {data_for_residual[2]} в коризине', reply_markup=markup)

    connection.commit()
    cursor.close()
    connection.close()
    bot.answer_callback_query(call.id)
    
    #print(call.message.caption)

#Лист товаров
def ProductSheet(call):
    bot.delete_message(call.message.chat.id, message_id = call.message.id)
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Каталог', callback_data='catalog_without_delete')
    btn2 = types.InlineKeyboardButton('Добавить в корзину', callback_data='get_in_shoppingcart')
    markup.row(btn1)
    markup.row(btn2)

    connection = sqlite3.connect('C:/WebAndTg/WebSite/backend/db.sqlite3', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM catalog WHERE Type = "{call.data}";')
    data = cursor.fetchall() 
    #print(data)
    for i in range(len(data)):
        
        bot.send_photo(call.message.chat.id, photo=data[i][4], caption=f'{data[i][2]} - {data[i][5]}$ \n{data[i][3]}', reply_markup=markup)

    cursor.close()
    connection.close()
    bot.answer_callback_query(call.id)
    
def buy(call):
    connection = sqlite3.connect('C:/WebAndTg/WebSite/backend/db.sqlite3', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM sales WHERE username=? AND product=? AND state=0', [call.message.chat.username, (call.message.caption).split(' ')[1]])
    data = cursor.fetchone()
    print(data)
    cursor.execute('UPDATE sales SET state = 1 WHERE username=? AND product=?', [call.message.chat.username, (call.message.caption).split(' ')[1]])
    bot.delete_message(call.message.chat.id, call.message.id)

    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Каталог', callback_data='catalog')
    markup.row(btn1)
    
    bot.send_message(call.message.chat.id, f'Вы купили {data[3]}шт {data[2]}', reply_markup=markup)
    connection.commit()
    cursor.close()
    connection.close()
    bot.answer_callback_query(call.id)

def buy_all(call):
    connection = sqlite3.connect('C:/WebAndTg/WebSite/backend/db.sqlite3', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM sales WHERE username=? AND state=0', [call.message.chat.username])
    data = cursor.fetchall()
    cursor.execute('UPDATE sales SET state = 1 WHERE username=?', [call.message.chat.username])
    bot.send_message(call.message.chat.id, 'Вы купили всю корзину')
    connection.commit()
    cursor.close()
    connection.close()
    bot.answer_callback_query(call.id)

def bought_product(call):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton('Каталог', callback_data='catalog_without_delete')
    markup.row(btn)
    connection = sqlite3.connect('C:/WebAndTg/WebSite/backend/db.sqlite3', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM sales WHERE username=? AND state=1', [call.message.chat.username])
    data = cursor.fetchall()
    
    for i in data:
        cursor.execute('SELECT * FROM catalog WHERE Model=?', [i[2]])
        
        data2 = cursor.fetchone()
        bot.send_photo(call.message.chat.id, photo = data2[4], caption=f'{i[3]}шт. - {i[2]} - {data2[5]}$ (шт)', reply_markup=markup)
        
    connection.commit()
    cursor.close()
    connection.close()

    bot.answer_callback_query(call.id)  

callback_map = {
    'delete_from_shoppingcart': delete_from_shoppingcart,
    'catalog': catalog,
    'catalog_without_delete': catalog_without_delete,
    'get_in_shoppingcart': get_in_shoppingcart,
    'help': help_function,
    'shoppingcart': shoppingcart,
    'Sneakers': ProductSheet,
    'Outwear': ProductSheet,
    'Jeans': ProductSheet,
    'buy': buy,
    'buy_all': buy_all,
    'bought_product': bought_product
}

bot.polling(none_stop=True)