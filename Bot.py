import os
import telebot
from flask import Flask, request

TOKEN = '1212381391:AAEJQ4gLSsVaay-2ZupoQteHh100qR0SkY0'
Bot = telebot.TeleBot(token=Token)
server = Flask(__name__)


def sendmsg(message,text):
    bot.send_message(message.chat.id,text)


@bot.message_handler(commands=['start'])
def startmsg(message):
    bot.send_message(message.chat.id,
                     '<b>Selamat Datang di E-Learning Bot UIN Sunan Gunung Djati Bandung</b>\n Silahkan Ketikkan <b> Hello </b> dan dapatkan balasan dari bot ini',
                     parse_mode='HTML')


@bot.message_handler(funct=lambda msg: msg.text is not None)
def replay_to_message(message):
    if 'Hello' in message.text.lower():
        sendmsg(message, 'Hai, {} Semoga Hari Mu Menyenangkan '.format(message.from_user.first_name))
    elif 'hello' in message.text.lower():
        sendmsg(message, 'Hai, {} Semoga Hari Mu Menyenangkan '.format(message.from_user.first_name))



#server
@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode('utf-8'))])
    return 'Ok... Webhook sudah terpasang ! ', 200


server.route('/')


def webhook():
    bot.remove_
    webhook()
    bot.set_webhook(url='https://elearningtelebot.herokuapp.com/' + TOKEN)
    return 'Ok... Webhook sudah terpasang ! ', 200


if __name__ == '__main__':
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))


