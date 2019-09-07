import telebot
from translator import Translate

bot = telebot.TeleBot("958018017:AAHo2IK1wJBnYGYT5Ml5tToE-PWMl8PkFqo")

@bot.message_handler(commands=["start", "help"])
def output(message):
    bot.send_message(message.chat.id, "A bot in development that translates English to Amharic")

@bot.message_handler(func=lambda message:True)
def all_reply(message):
    bot.send_message(message.chat.id, Translate(message.text))

bot.polling()