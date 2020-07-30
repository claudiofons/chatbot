import telepot
from Chatbot import Chatbot

telegram = telepot.Bot("coloque aqui seu token do telegram")
bot = Chatbot("apague o que está entre as aspas e de um nome ao seu bot")

def recebendoMsg(msg):
    frase = bot.escuta(frase=msg['text'])
    resp = bot.pensa(frase)
    bot.fala(resp)
    #chatID = msg['chat'] = ['id']
    tipoMsg, tipoChat, chatID = telepot.glance(msg)
    telegram.sendMessage(chatID, resp)

telegram.message_loop(recebendoMsg)

while True:
    pass
