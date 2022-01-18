import telebot
from pyowm import OWM

owm = OWM('your token here')
bot = telebot.TeleBot("your token here")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет, погода в каком городе Вас интересует?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(message.text)
        w = observation.weather
        temp = w.temperature('celsius')["temp"]

        answer = "В городе " + message.text + " сейчас " + str(temp)
    except:
        answer = "Проверьте правильность написания города"

    bot.send_message(message.chat.id, answer)


bot.polling()
