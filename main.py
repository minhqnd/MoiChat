import os
import logging
import telebot
import chat

logging.basicConfig(filename="bot.log", level=logging.INFO)

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

HELP_MESSAGE = """Các lệnh:
Không có lệnh gì đâu, cứ chat thôi
"""

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    reply_text = "Chào cu! Bố là <b>ChatBot</b> được tạo bởi Simsimi API 🤖\n\n"
    reply_text += HELP_MESSAGE

    reply_text += "\nGiờ muốn chat gì thì chat đi cu!"
    bot.send_message(message.chat.id, reply_text, parse_mode="HTML")


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    # bot.reply_to(message, response.sample_response(message.text))
    logterm = "Tin nhắn:", message.text, message.from_user.username
    responseChat = chat.send(message.text)
    print(logterm)
    logging.info(logterm)
    logging.info(responseChat)
    bot.send_chat_action(chat_id=message.chat.id, action='typing')
    bot.send_message(message.chat.id, responseChat)

bot.infinity_polling()