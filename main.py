import telebot
import os
from flask import Flask, request

TOKEN = os.getenv("8262690264:AAGaVnAZn1QPRbjR6jIhgAcJ9tohSORp7qs")
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

# Start komandasi
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Salom! Bu bot ishlayapti 🚀")

# Admin panel (faqat ID bo‘yicha)
ADMIN_ID = 6493383873  # bu yerga o‘zingning Telegram ID’ingni yozasan

@bot.message_handler(commands=['panel'])
def admin_panel(message):
    if message.chat.id == ADMIN_ID:
        bot.send_message(message.chat.id, "Admin panelga xush kelibsiz!")
    else:
        bot.send_message(message.chat.id, "Siz admin emassiz ❌")

# Render uchun server qismi
@server.route(f"/{TOKEN}", methods=["POST"])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=f"https://{os.getenv('kino-bot.onrender.com')}/{TOKEN}")
    return "Bot ishga tushdi!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
