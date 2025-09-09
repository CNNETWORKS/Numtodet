import requests
from telegram.ext import Updater, MessageHandler, Filters

BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
API_URL = "https://your-api-url.com/lookup"

def fetch_number_details(number):
    response = requests.get(f"{API_URL}?number={number}")
    if response.status_code == 200:
        return response.json()
    return {"error": "No details found"}

def handle_message(update, context):
    text = update.message.text.strip()
    if text.isdigit() and len(text) >= 7:
        details = fetch_number_details(text)
        update.message.reply_text(str(details))
    else:
        update.message.reply_text("Valid number bhejo.")

updater = Updater(token=BOT_TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
updater.start_polling()
updater.idle()
  
