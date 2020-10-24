import mqtt_module as m
import vars as v
import telebot
import datetime
import random
import time
#@Motobiker_bot token '1253875816:AAFLiQvsiMhDY34n9Lo4XmunLQ6j_URunx4'
#peppis bottoken
BOT_TOKEN = '1394807218:AAFf5OV7zqyRjRYqdeeh_rZn8eBXekM3Xso'

bot = telebot.TeleBot(BOT_TOKEN)
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('/start')
keyboard2 = telebot.types.ReplyKeyboardMarkup()
keyboard2.row('Get')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hi', reply_markup=keyboard2)

@bot.message_handler(content_types=['text'])
def send_text(message):
    append_log_file(message.text)
    # if message.text == 'Привет':
    #     bot.send_message(message.chat.id, 'Привет')

    # elif message.text == 'Пока':
    #     bot.send_message(message.chat.id, 'Прощай')
    if message.text == 'Get':
       # sendDocument
        doc = open('current.log', 'r')
        bot.send_document(message.chat.id, doc)
        doc.close()
        doc = open('all.log', 'r')
        bot.send_document(message.chat.id, doc)
        doc.close()
    # elif message.text == 'start game 2':
    #     # m.client.publish('Pub/targets_manager/run_game_2', '1')
    #     v.ttt = False
    # elif message.text == 'stop game 2':
    #     # m.client.publish('Pub/targets_manager/stop_game_2', '1')
    #     v.ttt = False
    # elif message.text == 'Demo':
    #     v.ttt = True
    #     demo()


def append_log_file(s):
    log_file = open('log.txt', 'a')
    s0 = datetime.datetime.now()
    log_file.write(s0.strftime("%d-%m-%Y %H:%M:%S") + '  ' + s + '\n')
    log_file.close()


def demo():

    t = 6
    p = 2
    i = 0
    while t <= 11:
        # m.client.publish('Pub/target_' + str(t)+'/' + 'Activate', str(p))
        t += 1
    t = 6
    while v.ttt:
        if t == 6:
            print
            m.client.publish('Pub/target_' + str(11)+'/' + 'Activate', str(p), qos=2)
        else:
            m.client.publish('Pub/target_' + str(t - 1) + '/' + 'Activate', str(p), qos=2)
        m.client.publish('Pub/target_' + str(t)+'/' + 'Deactivate', str(p), qos=2)
        i += 1
        t += 1
        if t == 12:
            t = 6
        print('Pub/target_' + str(t) +' '+ str(p))
        time.sleep(0.2)


# m.client.loop_start()
bot.polling()



