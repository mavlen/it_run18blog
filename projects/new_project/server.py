# # import telebot
# # import requests 

# bot = telebot.TeleBot('1949529391:AAEDSaoLIpa0YIqyvZHdIwkJvy4qFtP1NxE', parse_mode=None)
# url = 'https://api.telegram.org/bot1949529391:AAEDSaoLIpa0YIqyvZHdIwkJvy4qFtP1NxE/'

# response = requests.get(url+'getUpdates')
# for i in response.json()['result']:
#     print(i)

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you doing?")

# bot.polling()


# import telebot
# import requests


# url2 = "https://api.telegram.org/bot1949529391:AAEDSaoLIpa0YIqyvZHdIwkJvy4qFtP1NxE/sendMessage?chat_id=768745497&text=а я думал сова"

# for i in range(1000):
#     requests.get(url2)


# import telebot
# # import requests

# bot = telebot.TeleBot('1949529391:AAEDSaoLIpa0YIqyvZHdIwkJvy4qFtP1NxE',parse_mode=None)


# @bot.message_handler(content_types=['text'])
# def echo_all(message):
#     if message.text == 'Привет':
#         bot.reply_to(message,'Ассалам алейкум')
#     elif message.text == 'Пока':
#         bot.reply_to(message,'Даувай')

# bot.polling()


# import telebot
# from flask import Flask, request

# add = Flask(__name__)
# token = '1949529391:AAEDSaoLIpa0YIqyvZHdIwkJvy4qFtP1NxE'
# bot = telebot.TeleBot(token,parse_mode=None)

# @app.route("/",methods=['GET','HEAD'])
# def index():
#     return ''


# @bot.message_handler(commands=['help','start'])
# def send_welcome(message):
#     bot.reply_to(message,
#                   'Hi there,I am EchoBot./n')
#                   'I am here to echo your kind words back to you.')


# @bot.message_handler(func=lambda message: True,content_types=['text'])
# def echo_message(message):
#     bot.reply_to(message,message.text)

# # @app.

import telebot
import os
import uuid
from image import image_to_bw
import time

token = "1949529391:AAEDSaoLIpa0YIqyvZHdIwkJvy4qFtP1NxE"
bot = telebot.TeleBot(token,parse_mode=None)

# @server.route("/", methods=["POST"])
# def receive_update():
#  bot.process_new_updates(
#   [telebot.types.Update.de_json(request.stream.read().decode("utf-8"))]
#  )
#  return {'ok':True}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
 bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
 bot.reply_to(message, message.text)

@bot.message_handler(content_types=['photo'])
def photo(message):
    save_url = '/Users/Diana/projects/new_project/image'
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    image_name = str(uuid.uuid4())+'.jpg'
    downnloaded_file = bot.download_file(file_info.file_path)
    with open(save_url+image_name, 'wb')as new_file:
        new_file.write(downnloaded_file)
    path_to_bw = image_to_bw(save_url+image_name)
    img = open(path_to_bw, 'rb')
    bot.send_photo(message.chat.id, img)
    time.sleep(30)
    os.remove(path_to_bw) 

bot.polling()


# @server.route("/" + token, methods=["POST"])
# def getMessage():
#  bot.process_new_updates(
#   [
#    telebot.types.Update.de_json(
#     request.stream.read().decode("utf-8")
#    )
#   ]
#  )
#  return "!", 200

# if __name__ == "__main__":
#  server.run()
