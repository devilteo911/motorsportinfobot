# -*- coding: utf-8 -*-

import telegram
from telegram import ReplyKeyboardMarkup
from telegram.ext import Dispatcher, Updater, CommandHandler
import random
import requests
import json
import ast
import urllib3
from prettytable import PrettyTable
from emoji import emojize

bot_token = '697171712:AAFi2MjOvx0NFikgng3ukS0EL06IxIO9PvA'

my_bot = telegram.Bot(token=bot_token)
my_bot_updater = Updater(my_bot.token)


def start(bot, update, pass_chat_data=True):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id= chat_id, text= 'Hey, ora sono attivo 👨‍')
    bot.sendMessage(chat_id= chat_id, text = 'Se hai bisogno di aiuto, digita: /help')

def standings(bot, update,  pass_chat_data=True):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id, text = "Provvedo subito")
    url = 'https://ergast.com/api/' + 'f1/' + 'current' + '/' + 'last' + '/'+ 'driverStandings' + '.json'

    #Convert request in text
    req = requests.get(url).text

    #Convert json into data structure
    data_input = json.loads(req)

    #Removing the u' char
    datastore = ast.literal_eval(json.dumps(data_input))
    things = datastore['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
    i = 0

    #Inizializzo la tabella
    x = PrettyTable()
    #Indico quali sono i nomi delle colonne
    x.field_names = ['Pos', 'Nat', 'Driver', 'Team', 'Points']
    x.align['Team'] = 'c'

    with open('nationality'+'.json') as file:
        data_j = file.read()
    data_in = json.loads(data_j)

    #Cycle through the entire array of data taken from the JSON
    while datastore:
        try:
            nationality = data_in.get(things[i]['Driver']['nationality'])
            x.add_row([things[i]['position'],
                        emojize(':'+str(nationality)+':'),
                        things[i]['Driver']['code'],
                        things[i]['Constructors'][0]['constructorId'].capitalize(),
                        things[i]['points']])
            i = i+1
        except IndexError:
            break

    bot.sendMessage(chat_id, text = str(x))


def quali(bot, update, pass_chat_data=True):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id,'Risultati delle qualifiche in arrivo')
    url = 'https://ergast.com/api/' + 'f1/' + 'current' + '/' + 'last' + '/'+ 'qualifying' + '.json'
    req = requests.get(url).text
    data_input = json.loads(req)
    datastore = ast.literal_eval(json.dumps(data_input))
    things = datastore['MRData']['RaceTable']['Races'][0]['QualifyingResults']
    #circuit_name = things['Circuit']['circuitName']
    i=0
    y = PrettyTable()
    y.field_names = ['Pos', 'Driver', 'Q1', 'Q2', 'Q3']
    while datastore:
        try:
            if (i>9):
                y.add_row([things[i]['position'],
                                things[i]['Driver']['code'].upper(),
                                things[i]['Q1'],
                                emojize(':x:', use_aliases=True),
                                emojize(':x:', use_aliases=True)])
            else:
                y.add_row([things[i]['position'],
                                things[i]['Driver']['code'].upper(),
                                things[i]['Q1'],
                                things[i]['Q2'],
                                things[i]['Q3']])
            i =  i + 1
        except IndexError:
            break
    #print(y)
    bot.sendMessage(chat_id, text = str(y))

def race(bot, update, pass_chat_data=True):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id,'Risultati della gara in arrivo')
    url = 'https://ergast.com/api/' + 'f1/' + 'current' + '/' + 'last' + '/'+ 'results' + '.json'
    req = requests.get(url).text
    data_input = json.loads(req)
    datastore = ast.literal_eval(json.dumps(data_input))
    things = datastore['MRData']['RaceTable']['Races'][0]['Results']
    i=0
    z = PrettyTable()
    z.field_names = ['Pos', 'Driver','Status', 'Time']
    while datastore:
        try:
            if (things[i]['status'] == 'Finished'):
                z.add_row([things[i]['position'],
                           things[i]['Driver']['code'].upper(),
                           emojize(':checkered_flag:', use_aliases= True),
                           things[i]['Time']['time']])
            else:
                if(things[i]['status'][:1] == '+'):
                    z.add_row([things[i]['position'],
                               things[i]['Driver']['code'].upper(),
                               emojize(':checkered_flag:', use_aliases= True),
                               things[i]['status']])
                else:
                    z.add_row([things[i]['position'],
                               things[i]['Driver']['code'].upper(),
                               emojize(':x:', use_aliases=True),
                               things[i]['status']])
            i =  i + 1
        except IndexError:
            break
    #print(z)
    bot.sendMessage(chat_id, text = str(z))

def help_(bot, update, pass_chat_data=True):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id, text= 'Tutti i comandi, con relative descrizioni, sono disponibili digitando /   ')


#Handler
start_handler = CommandHandler('start', start)
standings_handler = CommandHandler('standings', standings)
qual_handler = CommandHandler('quali', quali)
race_handler = CommandHandler('race', race)
help_handler = CommandHandler('help', help_)
#Dispatcher
dispatcher = my_bot_updater.dispatcher

dispatcher.add_handler(start_handler)
dispatcher.add_handler(standings_handler)
dispatcher.add_handler(qual_handler)
dispatcher.add_handler(race_handler)
dispatcher.add_handler(help_handler)

my_bot_updater.start_polling()
my_bot_updater.idle()



while True:
    pass
