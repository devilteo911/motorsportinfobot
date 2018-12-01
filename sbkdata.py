from telegram import ReplyKeyboardMarkup, error


circuit_arr = ('AUS', 'THA', 'ESP', 'NED', 'ITA1', 'GBR', 'CZE', 'USA', 'ITA2', 'POR', 'FRA', 'ARG' , 'QAT')
keyboard = [['Australia', 'Thailand', 'Aragon', 'Dutch'], ['Italian'], ['UK', 'Czech', 'USA', 'Misano'], ['Portugal', 'France', 'Argentina' , 'Qatar']]


def race1(bot, update, pass_chat_data = True):
    global circuit_arr, keyboard
    chat_id = update.message.chat_id
    try:
        markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        bot.sendMessage(chat_id,text='Seleziona un gp', reply_markup=markup)
        url =  ''
        if(update.message.text == str('Australia')):
            url = 'http://resources.worldsbk.com/files/results/2018/' + str(circuit_arr[0]) + '/SBK/001/ALL/AllPdfs.pdf'
        elif(update.message.text == 'Thailand'):
            url = 'http://resources.worldsbk.com/files/results/2018/' + str(circuit_arr[1]) + '/SBK/001/ALL/AllPdfs.pdf'
        elif(update.message.text == 'Aragon'):
            url = 'http://resources.worldsbk.com/files/results/2018/' + str(circuit_arr[2]) + '/SBK/001/ALL/AllPdfs.pdf'
        elif(update.message.text == 'Dutch'):
            url = 'http://resources.worldsbk.com/files/results/2018/' + str(circuit_arr[3]) + '/SBK/001/ALL/AllPdfs.pdf'
        elif(update.message.text == 'Italian'):
            url = 'http://resources.worldsbk.com/files/results/2018/' + str(circuit_arr[4]) + '/SBK/001/ALL/AllPdfs.pdf'
        elif(update.message.text == 'UK'):
            url = 'http://resources.worldsbk.com/files/results/2018/' + str(circuit_arr[5]) + '/SBK/001/ALL/AllPdfs.pdf'
        elif(update.message.text == 'Czech'):
            url = 'http://resources.worldsbk.com/files/results/2018/' + str(circuit_arr[6]) + '/SBK/001/ALL/AllPdfs.pdf'
        elif(update.message.text == 'USA'):
            url = 'http://resources.worldsbk.com/files/results/2018/' + str(circuit_arr[7]) + '/SBK/001/ALL/AllPdfs.pdf'
        elif(update.message.text == 'Misano'):
            url = 'http://resources.worldsbk.com/files/results/2018/' + str(circuit_arr[8]) + '/SBK/001/ALL/AllPdfs.pdf'
        elif(update.message.text == 'Portugal'):
            url = 'http://resources.worldsbk.com/files/results/2018/' + str(circuit_arr[9]) + '/SBK/001/ALL/AllPdfs.pdf'
        elif(update.message.text == 'France'):
            url = 'http://resources.worldsbk.com/files/results/2018/' + str(circuit_arr[10]) + '/SBK/001/ALL/AllPdfs.pdf'
        elif(update.message.text == 'Argentina'):
            url = 'http://resources.worldsbk.com/files/results/2018/' + str(circuit_arr[11]) + '/SBK/001/ALL/AllPdfs.pdf'
        elif(update.message.text == 'Qatar'):
            url = 'http://resources.worldsbk.com/files/results/2018/' + str(circuit_arr[12]) + '/SBK/001/ALL/AllPdfs.pdf'
        #else:
            #update.message.reply_text('Penso tu abbia scritto qualcosa e non hai premuto i comandi della tastiera')
        bot.sendMessage(chat_id, text = 'Provvedo subito con i risultati gara 1 della SBK')
        bot.sendDocument(chat_id, document=url)
    except error.BadRequest:
        exit()

def race2(bot, update, pass_chat_data = True):
    global circuit_arr, keyboard
    chat_id = update.message.chat_id
    reply_markup = ReplyKeyboardMarkup(keyboard)
    bot.sendMessage(chat_id,text='Seleziona un gp', reply_markup=reply_markup)
    print(update.message.text)
    if(update.message.text == 'Australia'):
        print('sono qui')
        url = 'http://resources.worldsbk.com/files/results/2018/' + str(circuit_arr[0]) + '/SBK/002/ALL/AllPdfs.pdf'
    elif(update.message.text == 'Thailand'):
        url = 'http://resources.worldsbk.com/files/results/2018/' + str(circuit_arr[1]) + '/SBK/002/ALL/AllPdfs.pdf'
    elif(update.message.text == 'Aragon'):
        url = 'http://resources.worldsbk.com/files/results/2018/' + str(circuit_arr[2]) + '/SBK/002/ALL/AllPdfs.pdf'
    elif(update.message.text == 'Dutch'):
        url = 'http://resources.worldsbk.com/files/results/2018/' + str(circuit_arr[3]) + '/SBK/002/ALL/AllPdfs.pdf'
    elif(update.message.text == 'Italian'):
        url = 'http://resources.worldsbk.com/files/results/2018/' + str(circuit_arr[4]) + '/SBK/002/ALL/AllPdfs.pdf'
    elif(update.message.text == 'UK'):
        url = 'http://resources.worldsbk.com/files/results/2018/' + str(circuit_arr[5]) + '/SBK/002/ALL/AllPdfs.pdf'
    elif(update.message.text == 'Czech'):
        url = 'http://resources.worldsbk.com/files/results/2018/' + str(circuit_arr[6]) + '/SBK/002/ALL/AllPdfs.pdf'
    elif(update.message.text == 'USA'):
        url = 'http://resources.worldsbk.com/files/results/2018/' + str(circuit_arr[7]) + '/SBK/002/ALL/AllPdfs.pdf'
    elif(update.message.text == 'Misano'):
        url = 'http://resources.worldsbk.com/files/results/2018/' + str(circuit_arr[8]) + '/SBK/002/ALL/AllPdfs.pdf'
    elif(update.message.text == 'Portugal'):
        url = 'http://resources.worldsbk.com/files/results/2018/' + str(circuit_arr[9]) + '/SBK/002/ALL/AllPdfs.pdf'
    elif(update.message.text == 'France'):
        url = 'http://resources.worldsbk.com/files/results/2018/' + str(circuit_arr[10]) + '/SBK/002/ALL/AllPdfs.pdf'
    elif(update.message.text == 'Argentina'):
        url = 'http://resources.worldsbk.com/files/results/2018/' + str(circuit_arr[11]) + '/SBK/002/ALL/AllPdfs.pdf'
    elif(update.message.text == 'Qatar'):
        url = 'http://resources.worldsbk.com/files/results/2018/' + str(circuit_arr[12]) + '/SBK/002/ALL/AllPdfs.pdf'
    else:
        update.message.reply_text('Penso tu abbia scritto qualcosa e non hai premuto i comandi della tastiera')
    bot.sendMessage(chat_id, text = 'Provvedo subito con i risultati gara 2 della SBK')
    print(update.message.text)
    update.message.reply_document(url)