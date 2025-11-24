# kittybot/kittybot.py

from telebot import TeleBot

# Укажите токен, 
# который вы получили от @Botfather при создании бот-аккаунта:
bot = TeleBot(token='8254911274:AAFNWbrmJNuVS5nZ2-7HnacSRzskBxCZMU8')
# Укажите id своего аккаунта в Telegram:
chat_id = 412248518
message = 'Вам телеграмма!'
# Вызываем метод send_message, с помощью этого метода отправляются сообщения:
bot.send_message(chat_id, message)