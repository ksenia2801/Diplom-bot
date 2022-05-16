import telebot
from telebot import types


API_TOKEN = '5387469239:AAGcPJTX8FmFnaLnZ_YisGBdjfoYEL6Mo5o'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    item1 = types.KeyboardButton('Преподаватель')
    item2 = types.KeyboardButton('Студент')


    markup.add(item1, item2)

    bot.send_message(message.chat.id ,'Привет, {0.first_name} выбери кто ты студент или преподаватель !' .format(message.from_user), reply_markup = markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Преподаватель':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Введите фамилию',reply_markup = markup)


        elif message.text == 'Студент':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('РТФ')
            item2 = types.KeyboardButton('РКФ')
            item3 = types.KeyboardButton('ФСУ')
            item4 = types.KeyboardButton('ФВС')
            item5 = types.KeyboardButton('ФЭТ')
            item6 = types.KeyboardButton('ФИТ')
            item7 = types.KeyboardButton('ЭФ')
            item8 = types.KeyboardButton('ГФ')
            item9 = types.KeyboardButton('ЮФ')
            item10 = types.KeyboardButton('ФБ')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3,item4, item5, item6,item7, item8, item9,item10, back)

            bot.send_message(message.chat.id,'Выберите факультет',reply_markup = markup)

        elif message.text == 'Назад':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('Преподаватель')
                item2 = types.KeyboardButton('Студент')

                markup.add(item1, item2)

                bot.send_message(message.chat.id,'Выберите студент или преподаватель', reply_markup = markup)

        elif message.text == 'РТФ':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1-й')
                item2 = types.KeyboardButton('2-й')
                item3 = types.KeyboardButton('3-й')
                item4 = types.KeyboardButton('4-й')
                back = types.KeyboardButton('Назад')
                markup.add(item1, item2, item3, item4, back)

                bot.send_message(message.chat.id, 'Выберите курс', reply_markup=markup)

        elif message.text == '1-й':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('111')
                item2 = types.KeyboardButton('111-М-1')
                item3 = types.KeyboardButton('121-1')
                item4 = types.KeyboardButton('121-2')
                item5 = types.KeyboardButton('121-3')
                item6 = types.KeyboardButton('141-1')
                item7 = types.KeyboardButton('141-2')
                item8 = types.KeyboardButton('141-3')
                item9 = types.KeyboardButton('141-4')
                item10 = types.KeyboardButton('141-М2')
                item11 = types.KeyboardButton('141-М3')
                item12 = types.KeyboardButton('141-М4')
                item13 = types.KeyboardButton('141-М5')
                item14 = types.KeyboardButton('151')
                item15 = types.KeyboardButton('151-М')
                item16 = types.KeyboardButton('161')
                item17 = types.KeyboardButton('161-М')
                item18 = types.KeyboardButton('181-М')
                item19 = types.KeyboardButton('1А1')
                item20 = types.KeyboardButton('1А1-М')
                item21 = types.KeyboardButton('1В1')
                item22 = types.KeyboardButton('1В1-М')
                back = types.KeyboardButton('Назад')
                markup.add(item1, item2,item3, item4,item5, item6,item7, item8,item9, item10,item11, item12,item13, item14,item15, item16,item17, item18,item19, item20,item21, item22, back)

                bot.send_message(message.chat.id, 'Выберите номер группы', reply_markup=markup)

        elif message.text == '2-й':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('110')
                item2 = types.KeyboardButton('120-1')
                item3 = types.KeyboardButton('120-2')
                item4 = types.KeyboardButton('140-1')
                item5 = types.KeyboardButton('140-2')
                item6 = types.KeyboardButton('140-3')
                item7 = types.KeyboardButton('140-4')
                item8 = types.KeyboardButton('150')
                item9 = types.KeyboardButton('160')
                item10 = types.KeyboardButton('1А0')
                item11 = types.KeyboardButton('1В0')
                back = types.KeyboardButton('Назад')
                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11,back)

                bot.send_message(message.chat.id, 'Выберите номер группы', reply_markup=markup)


        elif message.text == 'РКФ':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1-й')
                item2 = types.KeyboardButton('2-й')
                item3 = types.KeyboardButton('3-й')
                item4 = types.KeyboardButton('4-й')
                back = types.KeyboardButton('Назад')
                markup.add(item1, item2, item3, item4, back)

                bot.send_message(message.chat.id, 'Выберите курс', reply_markup=markup)

        elif message.text == 'ФСУ':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1-й')
                item2 = types.KeyboardButton('2-й')
                item3 = types.KeyboardButton('3-й')
                item4 = types.KeyboardButton('4-й')
                back = types.KeyboardButton('Назад')
                markup.add(item1, item2, item3, item4, back)

                bot.send_message(message.chat.id, 'Выберите курс', reply_markup=markup)

        elif message.text == 'ФВС':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1-й')
                item2 = types.KeyboardButton('2-й')
                item3 = types.KeyboardButton('3-й')
                item4 = types.KeyboardButton('4-й')
                back = types.KeyboardButton('Назад')
                markup.add(item1, item2, item3, item4, back)

                bot.send_message(message.chat.id, 'Выберите курс', reply_markup=markup)

        elif message.text == 'ФЭТ':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1-й')
                item2 = types.KeyboardButton('2-й')
                item3 = types.KeyboardButton('3-й')
                item4 = types.KeyboardButton('4-й')
                back = types.KeyboardButton('Назад')
                markup.add(item1, item2, item3, item4, back)

                bot.send_message(message.chat.id, 'Выберите курс', reply_markup=markup)

        elif message.text == 'ФИТ':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1-й')
                item2 = types.KeyboardButton('2-й')
                item3 = types.KeyboardButton('3-й')
                item4 = types.KeyboardButton('4-й')
                back = types.KeyboardButton('Назад')
                markup.add(item1, item2, item3, item4, back)

                bot.send_message(message.chat.id, 'Выберите курс', reply_markup=markup)

        elif message.text == 'ЭФ':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1-й')
                item2 = types.KeyboardButton('2-й')
                item3 = types.KeyboardButton('3-й')
                item4 = types.KeyboardButton('4-й')
                back = types.KeyboardButton('Назад')
                markup.add(item1, item2, item3, item4, back)

                bot.send_message(message.chat.id, 'Выберите курс', reply_markup=markup)

        elif message.text == 'ГФ':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1-й')
                item2 = types.KeyboardButton('2-й')
                item3 = types.KeyboardButton('3-й')
                item4 = types.KeyboardButton('4-й')
                back = types.KeyboardButton('Назад')
                markup.add(item1, item2, item3, item4, back)

                bot.send_message(message.chat.id, 'Выберите курс', reply_markup=markup)

        elif message.text == 'ЮФ':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1-й')
                item2 = types.KeyboardButton('2-й')
                item3 = types.KeyboardButton('3-й')
                item4 = types.KeyboardButton('4-й')
                back = types.KeyboardButton('Назад')
                markup.add(item1, item2, item3, item4, back)

                bot.send_message(message.chat.id, 'Выберите курс', reply_markup=markup)

        elif message.text == 'ФБ':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1-й')
                item2 = types.KeyboardButton('2-й')
                item3 = types.KeyboardButton('3-й')
                item4 = types.KeyboardButton('4-й')
                back = types.KeyboardButton('Назад')
                markup.add(item1, item2, item3, item4, back)

                bot.send_message(message.chat.id, 'Выберите курс', reply_markup=markup)








bot.polling(none_stop=True)
