import paho.mqtt.client as mqtt
import vars as v
import configparser
import datetime
my_log = configparser.RawConfigParser()

#pay_load in topic 'log_file_append'
#START SYSTEM
#STOP SYSYTEM

#topics
# #/run_game_2
# #/run_game_1
# #/cons_beer_1
# #/cons_beer_2

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("Pub/targets_manager/#")

def on_message(client, userdata, msg):

    # if str(msg.payload).find("top"):
    str_t = str(msg.topic)
    str_m = str(msg.payload)[2:-1]

    print(str_t + "\n " + str_m)
    #     v.stat = msg.payload
    if str_t.find("log_file_append") >= 0:
        str_t = ''
        print('point 2')
        if str_m.find('START') >= 0:
            str_m = ''
            now = datetime.datetime.now()
            # print now.strftime("%d-%m-%Y %H:%M")
            my_log.read(v.current_log_file_name)
            my_log.set('current','date',now.strftime("%d-%m-%Y %H:%M"))
            my_log.set('current','total_beer_games','0')
            my_log.set('current','total_off_beer_games','0')
            my_log.set('current','cons_beer','0')
            my_log.set('current','end_time','0')
            my_log.write(open(v.current_log_file_name, "w"))
            my_log.clear()
        if str_m.find('STOP') >= 0:
            str_m = ''
            now = datetime.datetime.now()
            # print now.strftime("%d-%m-%Y %H:%M")
            my_log.read(v.current_log_file_name)
            my_log.set('current','end_time',now.strftime("%d-%m-%Y %H:%M"))
            my_log.write(open(v.current_log_file_name, "w"))
            my_log.clear()
            cur_file = open(v.current_log_file_name,'r')
            all_file = open(v.all_log_file_name,'a')
            all_file.write(cur_file.read())
            all_file.close()
            cur_file.close()

    if str_t.find('run') >= 0:
        str_t = ''
        print('point 1')
        if str_m == '0':
            my_log.read(v.current_log_file_name)
            g = my_log.getint('current','total_off_beer_games') + 1
            my_log.set('current','total_off_beer_games',g)
            my_log.write(open(v.current_log_file_name, "w"))
            my_log.clear()
        if str_m == '1':
            my_log.read(v.current_log_file_name)
            g = my_log.getint('current','total_beer_games') + 1
            my_log.set('current','total_beer_games',g)
            my_log.write(open(v.current_log_file_name, "w"))
            my_log.clear()
    
    if str_t.find("cons") >= 0:
        ml = float(str_m)
        my_log.read(v.current_log_file_name)
        g = round(my_log.getfloat('current','cons_beer') + ml/ 1000, 2) 
        my_log.set('current','cons_beer', g)
        my_log.write(open(v.current_log_file_name, "w"))
        my_log.clear()
    if str_t.find("delete_logs") >= 0:
        my_log.read(v.current_log_file_name)
        my_log.set('current','date', '0')
        my_log.set('current','total_beer_games','0')
        my_log.set('current','total_off_beer_games','0')
        my_log.set('current','cons_beer','0')
        my_log.set('current','end_time','0')
        my_log.write(open(v.current_log_file_name, "w"))
        my_log.clear()

        f = open(v.all_log_file_name,'w')
        f.write('')
        f.close()

            



def process_incoming_commands():
    client.loop()


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("127.0.0.1, 1883, 60")
# client.connect('192.168.2.2', 1883, 60)
client.loop_forever()
