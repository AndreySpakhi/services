import telebot

bot = telebot.TeleBot("your token here")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Привет мальчуки")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    
    if message.text.lower() == "здрасьте":
        answer = "Забор покрасьте"
    elif message.text.lower() == "шаришь за альт?":
        answer = "нет, я в комп не играю"
    elif message.text.lower() == "как дела?":
        answer = "нормально,а у тя как"
    elif message.text.lower() == "неплохо":
        answer = ":)" 
    
    elif message.text.lower() == "что делаешь":
        answer = "помогаю белке и лосю"   
    
    elif message.text.lower() == "круто":
        answer = "я бы не сказал " 
    elif message.text.lower() == "ты чжун ли ?":
        answer = "Osmanthus wine tastes the same as I remember... But where are those who share the memory? "      
     
    elif message.text.lower() == "а где бобби?":
        answer = "уехаль " 
     
    elif message.text.lower() == "пошли покурим?":
        answer = "на наше место? "
        
    elif message.text.lower() == "я ем":
        answer = "научи. " 
    elif message.text.lower() == "хорошо":
        answer = ":) " 
    elif message.text.lower() == "плохо":
        answer = ":("    
    else:
        answer = message.text
    bot.send_message(message.chat.id, answer)

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
	bot.send_message(message.chat.id, "Пожалуй, я сохраню это <3")

@bot.message_handler(content_types=['audio'])
def handle_audio(message):
	bot.send_message(message.chat.id, "Послушаю вечерком....может быть")

@bot.message_handler(content_types=['voice'])
def handle_voice(message):
	bot.send_message(message.chat.id, "Что ты там мурчишь?")

bot.polling()
