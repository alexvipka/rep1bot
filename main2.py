import sqlite3
import telebot
from telebot import types
from pyqiwip2p import QiwiP2P

text_start = '\n'.join(
    ['🤝🏻Добро пожаловать, вы получили доступ к этому боту, что бы оградить нас от нежелательных клиентов',
     '💯Вы попали туда куда нужно, открой доступ в новый мир🔐'])

text_dok = '\n'.join(
    ['✅Доказательства существования наших приватных каналов 😜 ⤵', 'https://cloud.mail.ru/public/E3R2/A5bJdB2Cp',
     '❗️Бот всегда будет доступен по этому адресу t.me/VipKaatg_bot'])
tarif = 'ℹВыбери необходимый тариф, нажав на соответствующую кнопку'
text_tar_1 = '\n'.join(
    ['Тариф: 😔 Мини 29₽', 'Цена: 29 RUB', 'Срок действия(дней): бессрочно', '', 'Описание тарифа:',
     '🌐Ссылка на облако', '💕𝕧𝕚𝕕𝕖𝕠 10 шт', '👧Возраста возраста 16-17 лет',
     '😶 Много тут не увидишь, так как это самый дешевый тариф', '', 'Тех.Поддержка @alexvipka',
     ])
text_tar_2 = '\n'.join(
    ['Тариф: 🤔 Не большой 50₽', 'Цена: 50 RUB', 'Срок действия(дней): бессрочно', '', 'Описание тарифа:',
     '🌐Ссылка на облако', '💕𝕧𝕚𝕕𝕖𝕠 30 шт', '👧Возраста возраста 14-17 лет', '', 'Тех.Поддержка @alexvipka',
     ])
text_tar_3 = '\n'.join(
    ['Тариф: 😈 Очень большой 79₽', 'Цена: 79 RUB', 'Срок действия(дней): бессрочно', '', 'Описание тарифа:',
     '🌐Ссылка на облако', '💕𝕧𝕚𝕕𝕖𝕠 100 шт', '👧Возраста возраста 11-17 лет', '', 'Тех.Поддержка @alexvipka',
     ])

token = '1839369136:AAE9h7_WdIYhyRzta2IwyBYRA31kAvtxuEs'
bot = telebot.TeleBot(token)

conn = sqlite3.connect('db.db', check_same_thread=False)
cursor = conn.cursor()

mm = types.ReplyKeyboardMarkup(row_width=2)  ##клава снизу
but1 = types.KeyboardButton("💵 Купить доступ")
but2 = types.KeyboardButton("⏳ Мои тарифы")
mm.add(but1, but2)

otvet = types.InlineKeyboardMarkup(row_width=1)  ## номера тарифов, расписаы
button1 = types.InlineKeyboardButton("😔 Мини 29₽", callback_data='tar1')
button2 = types.InlineKeyboardButton("🤔 Не большой 50₽", callback_data='tar2')
button3 = types.InlineKeyboardButton("😈 Очень большой 79₽", callback_data='tar3')
otvet.add(button1, button2, button3)


buy_1 = types.InlineKeyboardMarkup(row_width=1)
button1buy = types.InlineKeyboardButton("Купить", callback_data='buy1')
buy_1.add(button1buy)

buy_2 = types.InlineKeyboardMarkup(row_width=1)
button1buy = types.InlineKeyboardButton("Купить", callback_data='buy2')
buy_2.add(button1buy)

buy_3 = types.InlineKeyboardMarkup(row_width=1)
button1buy = types.InlineKeyboardButton("Купить", callback_data='buy3')
buy_3.add(button1buy)


def db_table_val(user_id: int, level1: int, level2: int, level3: int, nomer, name: str, num, chat_id):  # добавление нового пользователя в бд
    t = 'INSERT INTO tabl(id, level_1, level_2, level_3, lab, niktg, num, chat_id) VALUES(' + str(user_id) + ', ' + str(level1) + ', ' + str(
        level2) + ', ' + str(level3) + ', ' + str(nomer) + ', \'' + str(name) + '\', \'' + str(num) + '\', ' + str(chat_id) + ')'
    cursor.execute(t)
    conn.commit()

key = 'eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6InhpemRpZy0wMCIsInVzZXJfaWQiOiI3OTgyNzQxMjkyNSIsInNlY3JldCI6ImM5MjcwZTA1ZWNjZjMyOGQxZjYxYzk0YjVhMTJiNzVhNDFhZWJlNGNlZmQzNjI0NDVlOTI1NTdmYjQ1ZDdlN2MifX0='
p2p = QiwiP2P(auth_key=key)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, text_start, reply_markup=mm)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            now_id = call.message.chat.id
            if call.data == "tar1":
                bot.send_message(call.message.chat.id, text_tar_1, reply_markup=buy_1)
            if call.data == "tar2":
                bot.send_message(call.message.chat.id, text_tar_2, reply_markup=buy_2)
            if call.data == "tar3":
                bot.send_message(call.message.chat.id, text_tar_3, reply_markup=buy_3)

            if call.data == "dost":
                bot.send_message(call.message.chat.id, tarif, reply_markup=otvet)

            if call.data == "buy1":
                amount = 29
                lifetime = 5
                comment = 'Тариф Мини'
                bill = p2p.bill(amount=amount, lifetime=lifetime, comment=comment)
                link = bill.pay_url

                mini_opl = types.InlineKeyboardMarkup(row_width=1)
                button1 = types.InlineKeyboardButton(text='✅ Перейти к оплате', url=link)
                button2 = types.InlineKeyboardButton("⌛ Я оплатил", callback_data='check_opl_mini')
                mini_opl.add(button1, button2)

                bot.send_message(call.message.chat.id, 'Оплата 29 RUB\nСчет действителен 5 минут', reply_markup=mini_opl)
                t = "UPDATE tabl SET\nnum = \'" + str(bill.bill_id) + "\'\nWHERE id=" + str(now_id)
                cursor.execute(t)
                conn.commit()

            if call.data == "buy2":
                amount = 50
                lifetime = 5
                comment = 'Тариф Не большой'
                bill = p2p.bill(amount=amount, lifetime=lifetime, comment=comment)
                link = bill.pay_url

                mini_opl = types.InlineKeyboardMarkup(row_width=1)
                button1 = types.InlineKeyboardButton(text='✅ Перейти к оплате', url=link)
                button2 = types.InlineKeyboardButton("⌛ Я оплатил", callback_data='check_opl_neb')
                mini_opl.add(button1, button2)

                bot.send_message(call.message.chat.id, 'Оплата 50 RUB\nСчет действителен 5 минут', reply_markup=mini_opl)
                t = "UPDATE tabl SET\nnum = \'" + str(bill.bill_id) + "\'\nWHERE id=" + str(now_id)
                cursor.execute(t)
                conn.commit()

            if call.data == "buy3":
                amount = 79
                lifetime = 5
                comment = 'Тариф Очень большой'
                bill = p2p.bill(amount=amount, lifetime=lifetime, comment=comment)
                link = bill.pay_url

                mini_opl = types.InlineKeyboardMarkup(row_width=1)
                button1 = types.InlineKeyboardButton(text='✅ Перейти к оплате', url=link)
                button2 = types.InlineKeyboardButton("⌛ Я оплатил", callback_data='check_opl_big')
                mini_opl.add(button1, button2)

                bot.send_message(call.message.chat.id, 'Оплата 79 RUB\nСчет действителен 5 минут', reply_markup=mini_opl)
                t = "UPDATE tabl SET\nnum = \'" + str(bill.bill_id) + "\'\nWHERE id=" + str(now_id)
                cursor.execute(t)
                conn.commit()


            if call.data == 'check_opl_neb':
                result = cursor.execute("""SELECT * FROM tabl""").fetchall()
                for i in result:
                    if i[0] == now_id:
                        number = i[6]
                        status = p2p.check(bill_id=number).status
                        if status == 'PAID':
                            bot.send_message(call.message.chat.id, '🤝🏻 Оплата прошла успешно, ссылка на тариф в разделе ⏳ Мои тарифы')
                            t = "UPDATE tabl SET\nlevel_2 = 1\nWHERE id = " + str(now_id)
                            cursor.execute(t)
                            conn.commit()
                        else:
                            mini_opl = types.InlineKeyboardMarkup(row_width=1)
                            button2 = types.InlineKeyboardButton("⌛ Я оплатил", callback_data='check_opl_neb')
                            mini_opl.add(button2)
                            bot.send_message(call.message.chat.id, '🚫 Оплата не дошла до нас', reply_markup=mini_opl)

            if call.data == 'check_opl_mini':
                result = cursor.execute("""SELECT * FROM tabl""").fetchall()
                for i in result:
                    if i[0] == now_id:
                        number = i[6]
                        status = p2p.check(bill_id=number).status
                        if status == 'PAID':
                            bot.send_message(call.message.chat.id, '🤝🏻 Оплата прошла успешно, ссылка на тариф в разделе ⏳ Мои тарифы')
                            t = "UPDATE tabl SET\nlevel_1 = 1\nWHERE id = " + str(now_id)
                            cursor.execute(t)
                            conn.commit()
                        else:
                            mini_opl = types.InlineKeyboardMarkup(row_width=1)
                            button2 = types.InlineKeyboardButton("⌛ Я оплатил", callback_data='check_opl_mini')
                            mini_opl.add(button2)
                            bot.send_message(call.message.chat.id, '🚫 Оплата не дошла до нас', reply_markup=mini_opl)

            if call.data == 'check_opl_big':
                result = cursor.execute("""SELECT * FROM tabl""").fetchall()
                for i in result:
                    if i[0] == now_id:
                        number = i[6]
                        status = p2p.check(bill_id=number).status
                        if status == 'PAID':
                            bot.send_message(call.message.chat.id, '🤝🏻 Оплата прошла успешно, ссылка на тариф в разделе ⏳ Мои тарифы')
                            t = "UPDATE tabl SET\nlevel_3 = 1\nWHERE id = " + str(now_id)
                            cursor.execute(t)
                            conn.commit()
                        else:
                            mini_opl = types.InlineKeyboardMarkup(row_width=1)
                            button2 = types.InlineKeyboardButton("⌛ Я оплатил", callback_data='check_opl_big')
                            mini_opl.add(button2)
                            bot.send_message(call.message.chat.id, '🚫 Оплата не дошла до нас', reply_markup=mini_opl)

    except Exception as e:
        print(repr(e))


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    result = cursor.execute("""SELECT * FROM tabl""").fetchall()
    now_id = message.from_user.id
    if now_id not in list(map(lambda x: x[0], result)):
        us_id = now_id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username
        level1 = 0
        level2 = 0
        level3 = 0
        chat_id = message.chat.id
        db_table_val(user_id=us_id, level1=level1, level2=level2, level3=level3, nomer=0, name=username, num=0, chat_id=chat_id)
    result = cursor.execute("""SELECT * FROM tabl""").fetchall()
    for i in result:
        if i[0] == now_id:
            level1, level2, level3 = i[1:4]
    if message.text == 'убери':
        bot.send_message(message.chat.id, 'ок(', reply_markup=types.ReplyKeyboardRemove())
    elif message.text == '💵 Купить доступ':
        bot.send_message(message.chat.id, tarif, reply_markup=otvet)
    elif message.text == '⏳ Мои тарифы':
        otvet2 = types.InlineKeyboardMarkup(row_width=1)  ## ссылки на тарифы
        btn1 = types.InlineKeyboardButton(text='😔 Мини 29₽', url='https://vk.com/jeka_skob24')
        btn2 = types.InlineKeyboardButton(text='🤔 Не большой 50₽', url='https://vk.com/jeka_skob24')
        btn3 = types.InlineKeyboardButton(text='😈 Очень большой 79₽', url='https://vk.com/jeka_skob24')
        btn4 = types.InlineKeyboardButton("💵 Купить доступ", callback_data='dost')
        t2 = ['📝 Ваши подписки:']
        if level1 == 1:
            t2.append('канал: 😔 Мини 29₽')
            t2.append('цена: 29 RUB')
            t2.append('')
            otvet2.add(btn1)
        if level2 == 1:
            t2.append('канал: 🤔 Не большой 50₽')
            t2.append('цена: 50 RUB')
            t2.append('')
            otvet2.add(btn2)
        if level3 == 1:
            t2.append('канал: 😈 Очень большой 79₽')
            t2.append('цена: 79 RUB')
            t2.append('')
            otvet2.add(btn3)
        otvet2.add(btn4)
        if level1 + level2 + level3 == 0:
            t2.append('Пока что пусто')
        else:
            t2.append('ℹ️ Для перехода в канал, нажмите на соотвествущую кнопку')
        t2 = '\n'.join(t2)
        bot.send_message(message.chat.id, t2, reply_markup=otvet2)


    else:
        bot.send_message(now_id, 'Введите /start')


bot.polling(none_stop=True)
