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
                item5 = types.KeyboardButton('5-й')
                back = types.KeyboardButton('Назад')
                markup.add(item1, item2, item3, item4,item5, back)

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

        elif message.text == '3-й':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('119')
            item2 = types.KeyboardButton('129')
            item3 = types.KeyboardButton('149-1')
            item4 = types.KeyboardButton('149-2')
            item5 = types.KeyboardButton('149-3')
            item6 = types.KeyboardButton('149-4')
            item7 = types.KeyboardButton('159')
            item8 = types.KeyboardButton('169')
            item9 = types.KeyboardButton('1А9')
            item10 = types.KeyboardButton('1В9')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, back)

            bot.send_message(message.chat.id, 'Выберите номер группы', reply_markup=markup)

        elif message.text == '4-й':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('118')
            item2 = types.KeyboardButton('128')
            item3 = types.KeyboardButton('148-1')
            item4 = types.KeyboardButton('148-2')
            item5 = types.KeyboardButton('148-3')
            item6 = types.KeyboardButton('148-4')
            item7 = types.KeyboardButton('158')
            item8 = types.KeyboardButton('168')
            item9 = types.KeyboardButton('1А8')
            item10 = types.KeyboardButton('1В9')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, back)

            bot.send_message(message.chat.id, 'Выберите номер группы', reply_markup=markup)

        elif message.text == '5-й':
             markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
             item1 = types.KeyboardButton('127-1')
             back = types.KeyboardButton('Назад')
             markup.add(item1, back)

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

        elif message.text == '1-й':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('201-1')
            item2 = types.KeyboardButton('201-2')
            item3 = types.KeyboardButton('211')
            item4 = types.KeyboardButton('221-1')
            item5 = types.KeyboardButton('221-2')
            item6 = types.KeyboardButton('231-1')
            item7 = types.KeyboardButton('231-2')
            item8 = types.KeyboardButton('231-3')
            item9 = types.KeyboardButton('231-4')
            item10 = types.KeyboardButton('231-5')
            item11 = types.KeyboardButton('231-6')
            item12 = types.KeyboardButton('261-М1')
            item13 = types.KeyboardButton('261-М2')
            item14 = types.KeyboardButton('271-М1')
            item15 = types.KeyboardButton('271-М2')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10,item11, item12, item13, item14, item15, back)

            bot.send_message(message.chat.id, 'Выберите номер группы', reply_markup=markup)

        elif message.text == '2-й':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('200')
            item2 = types.KeyboardButton('210')
            item3 = types.KeyboardButton('220')
            item4 = types.KeyboardButton('230-1')
            item5 = types.KeyboardButton('230-2')
            item6 = types.KeyboardButton('230-3')
            item7 = types.KeyboardButton('230-4')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4, item5, item6, item7, back)

            bot.send_message(message.chat.id, 'Выберите номер группы', reply_markup=markup)

        elif message.text == '3-й':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('209')
            item2 = types.KeyboardButton('219-1')
            item3 = types.KeyboardButton('219-2')
            item4 = types.KeyboardButton('229-1')
            item5 = types.KeyboardButton('239-1')
            item6 = types.KeyboardButton('239-2')
            item7 = types.KeyboardButton('239-3')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4, item5, item6, item7, back)

            bot.send_message(message.chat.id, 'Выберите номер группы', reply_markup=markup)

        elif message.text == '4-й':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('208')
            item2 = types.KeyboardButton('218-1')
            item3 = types.KeyboardButton('218-2')
            item4 = types.KeyboardButton('228-1')
            item5 = types.KeyboardButton('238-1')
            item6 = types.KeyboardButton('238-2')
            item7 = types.KeyboardButton('238-3')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4, item5, item6, item7, back)

            bot.send_message(message.chat.id, 'Выберите номер группы', reply_markup=markup)

        elif message.text == 'ФСУ':
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
            item1 = types.KeyboardButton('401-1')
            item2 = types.KeyboardButton('401-M')
            item3 = types.KeyboardButton('421-1')
            item4 = types.KeyboardButton('421-2')
            item5 = types.KeyboardButton('421-3')
            item6 = types.KeyboardButton('421-4')
            item7 = types.KeyboardButton('421-M1')
            item8 = types.KeyboardButton('431-1')
            item9 = types.KeyboardButton('431-2')
            item10 = types.KeyboardButton('431-3')
            item11 = types.KeyboardButton('431-M1')
            item12 = types.KeyboardButton('431-М2')
            item13 = types.KeyboardButton('441-1')
            item14 = types.KeyboardButton('441-2')
            item15 = types.KeyboardButton('471-1')
            item16 = types.KeyboardButton('471-М')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10,item11, item12, item13, item14, item15,item16, back)

            bot.send_message(message.chat.id, 'Выберите номер группы', reply_markup=markup)

        elif message.text == '2-й':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('400-1')
            item2 = types.KeyboardButton('420-1')
            item3 = types.KeyboardButton('420-2')
            item4 = types.KeyboardButton('420-3')
            item5 = types.KeyboardButton('420-4')
            item6 = types.KeyboardButton('430-1')
            item7 = types.KeyboardButton('430-2')
            item8 = types.KeyboardButton('430-3')
            item9 = types.KeyboardButton('430-4')
            item10 = types.KeyboardButton('440-1')
            item11 = types.KeyboardButton('440-2')
            item12 = types.KeyboardButton('470-1')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, back)

            bot.send_message(message.chat.id, 'Выберите номер группы', reply_markup=markup)

        elif message.text == '3-й':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('409-1')
            item2 = types.KeyboardButton('429-1')
            item3 = types.KeyboardButton('429-2')
            item4 = types.KeyboardButton('429-3')
            item5 = types.KeyboardButton('439-1')
            item6 = types.KeyboardButton('439-2')
            item7 = types.KeyboardButton('439-3')
            item8 = types.KeyboardButton('439-4')
            item9 = types.KeyboardButton('439-5')
            item10 = types.KeyboardButton('449-1')
            item11 = types.KeyboardButton('449-2')
            item12 = types.KeyboardButton('479-1')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, back)

            bot.send_message(message.chat.id, 'Выберите номер группы', reply_markup=markup)

        elif message.text == '4-й':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('408')
            item2 = types.KeyboardButton('428-1')
            item3 = types.KeyboardButton('428-2')
            item4 = types.KeyboardButton('428-3')
            item5 = types.KeyboardButton('438-1')
            item6 = types.KeyboardButton('438-2')
            item7 = types.KeyboardButton('438-3')
            item8 = types.KeyboardButton('448-1')
            item9 = types.KeyboardButton('478-1')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, back)

            bot.send_message(message.chat.id, 'Выберите номер группы', reply_markup=markup)



        elif message.text == 'ФВС':
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
            item1 = types.KeyboardButton('511-1')
            item2 = types.KeyboardButton('511-M')
            item3 = types.KeyboardButton('521')
            item4 = types.KeyboardButton('531')
            item5 = types.KeyboardButton('541-1')
            item6 = types.KeyboardButton('541-M')
            item7 = types.KeyboardButton('551-M')
            item8 = types.KeyboardButton('571-1')
            item9 = types.KeyboardButton('571-2')
            item10 = types.KeyboardButton('581')
            item11 = types.KeyboardButton('581-M')
            item12 = types.KeyboardButton('591-1')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, back)

            bot.send_message(message.chat.id, 'Выберите номер группы', reply_markup=markup)

        elif message.text == '2-й':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('510-1')
            item2 = types.KeyboardButton('520')
            item3 = types.KeyboardButton('530-1')
            item4 = types.KeyboardButton('540')
            item5 = types.KeyboardButton('580-1')
            item6 = types.KeyboardButton('580-2')
            item7 = types.KeyboardButton('580-3')
            item8 = types.KeyboardButton('590-1')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, back)

            bot.send_message(message.chat.id, 'Выберите номер группы', reply_markup=markup)

        elif message.text == '3-й':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('519-1')
            item2 = types.KeyboardButton('519-2')
            item3 = types.KeyboardButton('529')
            item4 = types.KeyboardButton('539-1')
            item5 = types.KeyboardButton('549')
            item6 = types.KeyboardButton('589-1')
            item7 = types.KeyboardButton('589-2')
            item8 = types.KeyboardButton('589-3')
            item9 = types.KeyboardButton('599-1')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, back)

            bot.send_message(message.chat.id, 'Выберите номер группы', reply_markup=markup)

        elif message.text == '4-й':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('518-1')
            item2 = types.KeyboardButton('518-2')
            item3 = types.KeyboardButton('528')
            item4 = types.KeyboardButton('538')
            item5 = types.KeyboardButton('548-1')
            item6 = types.KeyboardButton('588-1')
            item7 = types.KeyboardButton('588-2')
            item8 = types.KeyboardButton('588-3')
            item9 = types.KeyboardButton('598-1')
            item10 = types.KeyboardButton('598-2')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9,item10, back)

            bot.send_message(message.chat.id, 'Выберите номер группы', reply_markup=markup)

        elif message.text == 'ФЭТ':
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
            item1 = types.KeyboardButton('311-1')
            item2 = types.KeyboardButton('311-2')
            item3 = types.KeyboardButton('311-M')
            item4 = types.KeyboardButton('321-1')
            item5 = types.KeyboardButton('321-2')
            item6 = types.KeyboardButton('341')
            item7 = types.KeyboardButton('341-M')
            item8 = types.KeyboardButton('351-1')
            item9 = types.KeyboardButton('351-M')
            item10 = types.KeyboardButton('361-1')
            item11 = types.KeyboardButton('361-2')
            item12 = types.KeyboardButton('361-3')
            item13 = types.KeyboardButton('361-M1')
            item14 = types.KeyboardButton('361-M2')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, back)

            bot.send_message(message.chat.id, 'Выберите курс', reply_markup=markup)

        elif message.text == '2-й':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('310')
            item2 = types.KeyboardButton('320-1')
            item3 = types.KeyboardButton('320-2')
            item4 = types.KeyboardButton('340')
            item5 = types.KeyboardButton('350')
            item6 = types.KeyboardButton('360-1')
            item7 = types.KeyboardButton('360-2')
            item8 = types.KeyboardButton('360-4')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, back)

            bot.send_message(message.chat.id, 'Выберите номер группы', reply_markup=markup)

        elif message.text == '3-й':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('319')
            item2 = types.KeyboardButton('329-1')
            item3 = types.KeyboardButton('349')
            item4 = types.KeyboardButton('359')
            item5 = types.KeyboardButton('369-1')
            item6 = types.KeyboardButton('369-2')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4, item5, item6, back)

            bot.send_message(message.chat.id, 'Выберите номер группы', reply_markup=markup)

        elif message.text == '4-й':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('318')
            item2 = types.KeyboardButton('328-1')
            item3 = types.KeyboardButton('348-1')
            item4 = types.KeyboardButton('358')
            item5 = types.KeyboardButton('368-1')
            item6 = types.KeyboardButton('368-2')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4, item5, item6, back)

            bot.send_message(message.chat.id, 'Выберите номер группы', reply_markup=markup)

        elif message.text == 'ФИТ':
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
            item1 = types.KeyboardButton('011')
            item2 = types.KeyboardButton('011-M')
            item3 = types.KeyboardButton('021-1')
            item4 = types.KeyboardButton('031-M')
            item5 = types.KeyboardButton('051')
            item6 = types.KeyboardButton('051-М')
            item7 = types.KeyboardButton('ИП021-1')
            item8 = types.KeyboardButton('ИП021-2')
            item9 = types.KeyboardButton('ИП021-3')
            item10 = types.KeyboardButton('ИП021-4')
            item11 = types.KeyboardButton('ИП021-5')
            item12 = types.KeyboardButton('ИП021-6')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, back)

            bot.send_message(message.chat.id, 'Выберите номер группы', reply_markup=markup)

        elif message.text == '2-й':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('010')
            item2 = types.KeyboardButton('050')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, back)

            bot.send_message(message.chat.id, 'Выберите номер группы', reply_markup=markup)

        elif message.text == '3-й':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('019')
            item2 = types.KeyboardButton('059')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, back)

            bot.send_message(message.chat.id, 'Выберите номер группы', reply_markup=markup)

        elif message.text == '2-й':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('018')
            back = types.KeyboardButton('Назад')
            markup.add(item1, back)

            bot.send_message(message.chat.id, 'Выберите номер группы', reply_markup=markup)



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
