import configparser
import datetime
import vars as v
my_log = configparser.RawConfigParser()
now = datetime.datetime.now()
# print now.strftime("%d-%m-%Y %H:%M")
my_log.read(v.current_log_file_name)
my_log.set('current','end_time',now.strftime("%d-%m-%Y %H:%M"))
my_log.write(open(v.current_log_file_name, "w"))
cur_file = open(v.current_log_file_name,'r')
all_file = open(v.all_log_file_name,'a')
all_file.write(cur_file.read())
all_file.close()
cur_file.close()