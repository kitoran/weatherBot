# coding='utf-8'
from telegram import Updater
import requests as r
import json

#tree = ET.fromstring(r.get('https://pogoda.yandex.ru/static/cities.xml').text)
appid = '7d734b682f355f9b477c153cf537fa6b'
#print(weather)
updater = Updater(token='202926389:AAGRNu6MExzKd6CB3NSWIZYBax85GjsS8tM')
dispatcher = updater.dispatcher
def start(bot, update):
   bot.sendMessage(chat_id=update.message.chat_id, text="i'm weather bot")
dispatcher.addTelegramCommandHandler('start', start)
updater.start_polling()

#pwl = enchant.request_pwl_dict("mywords.txt")


def echo(bot, update):
   town = update.message.text
   purexml = r.get('http://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s' % (town, appid)).text
   weather = json.loads(purexml)["weather"][0]["main"].lower()
   town = json.loads(purexml)["name"]
   bot.sendMessage(chat_id=update.message.chat_id, text="it's " + weather + " in " + town)

dispatcher.addTelegramMessageHandler(echo)


def help(bot, update, args):
   bot.sendMessage(chat_id=update.message.chat_id, text="type town name to see weather there")

dispatcher.addTelegramCommandHandler('help', help)