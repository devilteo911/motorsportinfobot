# -*- coding: utf-8 -*-

import telegram
import logging
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import Dispatcher, Updater, CommandHandler, MessageHandler, Filters
from f1data import standings, race, quali, constStandings
from sbkdata import race1, race2


bot_token = '697171712:AAFi2MjOvx0NFikgng3ukS0EL06IxIO9PvA'

my_bot = telegram.Bot(token=bot_token)
my_bot_updater = Updater(my_bot.token)

print(logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

def start(bot, update, pass_chat_data=True):
    chat_id = update.message.chat_id
    print('New user:' + str(chat_id))
    user = update.message.from_user.last_name
    user_arr = []
    count = len(user_arr) + 1
    if chat_id not in user_arr:
        user_arr.append((str(user), chat_id, count))
    print(user_arr)
    keys = [['F1', 'SBK', 'Help']]
    markup = ReplyKeyboardMarkup(keys, resize_keyboard=True)
    bot.sendMessage(chat_id=chat_id, text='Hey, ora sono attivo 👨‍', reply_markup=markup)
    if update.message.text == 'SBK':
        selectCat(my_bot, update)
    elif update.message.text == 'Help':
        update.message.reply_text('La tastiera custom sará la tua migliore amica')

def selectCat(bot, update, pass_chat_data=True):
    chat_id = update.message.chat_id
    keys = [['Gara1', 'Gara2', 'Indietro']]
    markup = ReplyKeyboardMarkup(keys, resize_keyboard=True)
    bot.sendMessage(chat_id, text='Seleziona la gara', reply_markup=markup)
    if update.message.text == 'Gara1':
        race1(my_bot, update)
    elif update.message.text == 'Gara2':
        race2(my_bot, update)
    elif update.message.text == 'Indietro':
        start(my_bot, update)
    else:
        update.message.reply_text('Mmmmh')


#Handler
start_handler = CommandHandler('start', start)
standings_handler = CommandHandler('standings', standings)
constStandings_handler = CommandHandler('cstandings', constStandings)
qual_handler = CommandHandler('quali', quali)
race_handler = CommandHandler('race', race)
#Dispatcher
dispatcher = my_bot_updater.dispatcher

dispatcher.add_handler(start_handler)
dispatcher.add_handler(standings_handler)
dispatcher.add_handler(constStandings_handler)
dispatcher.add_handler(qual_handler)
dispatcher.add_handler(race_handler)
dispatcher.add_handler(MessageHandler(Filters.text, selectCat))
dispatcher.add_handler(MessageHandler(Filters.text, race1))
dispatcher.add_handler(MessageHandler(Filters.text, race2))

my_bot_updater.start_polling()
my_bot_updater.idle()



while True:
    pass
