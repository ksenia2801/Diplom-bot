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
            bot.send_message(message.chat.id, 'Введите фамилию',reply_markup = markup)

        elif message.text == 'Студент':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('ФСУ')
            item2 = types.KeyboardButton('ФВС')
            item3 = types.KeyboardButton('РТФ')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, back)

            bot.send_message(message.chat.id,'Выберите факультет',reply_markup = markup)

        elif message.text == 'Назад':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('Преподаватель')
                item2 = types.KeyboardButton('Студент')

                markup.add(item1, item2)

                bot.send_message(message.chat.id,'Назад',reply_markup = markup)




bot.polling(none_stop=True)
