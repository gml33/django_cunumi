import telebot
import os

TOKEN = os.environ.get('TOKEN')

bot = telebot.TeleBot(TOKEN)
channel_id = chat_id = os.environ.get('channel_id')
chat_id = os.environ.get('chat_id')

#bot.send_message(chat_id, text='Iniciando servidor CUNUMI')