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




bot.polling(none_stop=True)
