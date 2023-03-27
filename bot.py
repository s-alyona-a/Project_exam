import telebot  # импортируем модуль pyTelegramBotAPI
import conf     # импортируем наш секретный токен
import new_model_test as nmt
from telebot import types
import random

# telebot.apihelper.proxy = conf.PROXY # если нет проблем с блокировкой, удалите эту строку
bot = telebot.TeleBot(conf.TOKEN)  # создаем экземпляр бота

with open("stickers_id.txt") as stick_f:
    id_list = stick_f.readlines()

# этот обработчик запускает функцию send_welcome, когда пользователь отправляет команды /start или /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Здравствуйте! Это бот, который поговорит с вами, как Дюма.")
    # создаем клавиатуру
    markup = types.ReplyKeyboardMarkup(row_width=1) # по умолчанию 3
    itembtna = types.KeyboardButton('/start')
    itembtnb = types.KeyboardButton('/phrase')
    itembtnc = types.KeyboardButton('/who_r_u_2day')
    markup.row(itembtna, itembtnb, itembtnc)

    # отправляем сообщение пользователю
    bot.send_message(message.chat.id, "Нажмите кнопку!", reply_markup=markup)

@bot.message_handler(commands=['phrase'])
def ask_length(message):
    # создаем клавиатуру
    keyboard = types.InlineKeyboardMarkup()
    itembtna = types.InlineKeyboardButton(text="25", callback_data="25")
    itembtnb = types.InlineKeyboardButton(text="50", callback_data="50")
    itembtnc = types.InlineKeyboardButton(text="75", callback_data="75")
    itembtnd = types.InlineKeyboardButton(text="100", callback_data="100")
    keyboard.row(itembtna, itembtnb)
    keyboard.row(itembtnc, itembtnd)

    # отправляем сообщение пользователю
    bot.send_message(message.chat.id, "Выберите, сколько символов хотите", reply_markup=keyboard)

# функция запустится, когда пользователь нажмет на кнопку
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        bot.send_message(call.message.chat.id, nmt.res(call.data))

@bot.message_handler(commands=['who_r_u_2day'])
def sticker(message):
    nmb = random.randint(0, 54)
    bot.send_sticker(message.chat.id, id_list[nmb].strip())

@bot.message_handler(content_types=["text"])
def photo(message):
    cif = random.randint(0, 2)
    if cif == 0:
        photo = open('what1.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        video = open('what2.gif', 'rb')
        bot.send_video(message.chat.id, video)


bot.polling(none_stop=True)