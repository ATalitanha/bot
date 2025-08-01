import os
from telegram import Bot

TOKEN = os.environ["BOT_TOKEN"]
APP_URL = os.environ["APP_URL"]

bot = Bot(token=TOKEN)
webhook_url = f"{APP_URL}/webhook"

bot.set_webhook(url=webhook_url)
print(f"Webhook set to: {webhook_url}")
