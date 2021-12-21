import os
import telebot


token = '5048476337:AAHNgTxLHtHfDHuUm-PdOksvm6aJlr0gp-k'
bot = telebot.TeleBot(token)



@bot.message_handler(commands=['start'])
def start_welcom(message):
    name = message.from_user.first_name
    welcome = f'Дарова {name}\nМеня зовут Алекс'
    sticer  = open('D:/Ziko/Проекты/koperayting_bot/text/telegram_version/all_files/hello.webp', 'rb')
    bot.send_message(message.chat.id, welcome)
    print(message.text)

bot.polling()
