# -*- coding: utf-8 -*-
import requests
import urllib3
import json
import ast
import time
from prettytable import PrettyTable
from emoji import emojize

day = time.strftime('%a')
month = time.strftime('%b')


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

    #Initialize the table
    x = PrettyTable()
    #Assigning column names
    x.field_names = ['Pos', 'Nat', 'Driver', 'Team', 'Points']
    x.align['Team'] = 'c'

    #With construct to open the json, read it and transform it in array of elements
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
    totRounds = 21
    remRounds = totRounds - int(datastore['MRData']['StandingsTable']['StandingsLists'][0]['round'])
    currSeason = datastore['MRData']['StandingsTable']['StandingsLists'][0]['season']
    diffPoints = int(things[0]['points'])-int(things[1]['points'])
    totPuntiRim = remRounds*25
    bot.sendMessage(chat_id, text = str(x))

    if(diffPoints > totPuntiRim):
        bot.sendMessage(chat_id, text = str(things[0]['Driver']['familyName'] + ' è il campione del mondo della stagione '+ currSeason +
                        ' con ' + str(remRounds)+ ' di anticipo!'))
    else:
        bot.sendMessage(chat_id, text = str('Il margine di ' + things[0]['Driver']['familyName'] + ' su ' +
                    things[1]['Driver']['familyName']+ ' è di ' +str(diffPoints)+ ' punti. '
                    + 'Mancano ancora ' + str(remRounds)+ ' gare, per un totale di ' + str(totPuntiRim) +' punti in palio.'))


def constStandings(bot, update, pass_chat_data = True):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id, text = 'Classifica costruttori in arrivo')

    url = 'http://ergast.com/api/f1/current/last/constructorStandings.json'
    req = requests.get(url).text
    data_input = json.loads(req)
    datastore = ast.literal_eval(json.dumps(data_input))
    things = datastore['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings']

    i=0
    h = PrettyTable()
    h.field_names = ['Pos', 'Constructor', 'Points', 'Wins']

    while datastore:
        try:
            h.add_row([things[i]['position'],
                        things[i]['Constructor']['name'],
                        things[i]['points'],
                        things[i]['wins']])
            i = i+1
        except IndexError:
            break
    #print(h)
    bot.sendMessage(chat_id, text = str(h))



def quali(bot, update, pass_chat_data=True):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id,'Risultati delle qualifiche in arrivo')
    if (str(day) == 'Sat'):
        url = 'https://ergast.com/api/' + 'f1/' + 'current' + '/' + 'next' + '/'+ 'qualifying' + '.json'
        #print('next', url)
    else:
        url = 'https://ergast.com/api/' + 'f1/' + 'current' + '/' + 'last' + '/'+ 'qualifying' + '.json'
        #print('last', url)
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
            if (i>13):
                y.add_row([things[i]['position'],
                                things[i]['Driver']['code'].upper(),
                                things[i]['Q1'],
                                emojize(':x:', use_aliases=True),
                                emojize(':x:', use_aliases=True)])
            elif (i>9 and i<=13):
                y.add_row([things[i]['position'],
                                things[i]['Driver']['code'].upper(),
                                things[i]['Q1'],
                                things[i]['Q2'],
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


#http://ergast.com/api/f1/drivers/

