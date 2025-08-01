from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import (
    Application, CommandHandler, ContextTypes,
    MessageHandler, filters
)
import os

TOKEN = os.environ["BOT_TOKEN"]
WEBHOOK_SECRET = os.environ["WEBHOOK_SECRET"]
APP_URL = os.environ["APP_URL"]  # بدون اسلش آخر

app = FastAPI()

telegram_app = Application.builder().token(TOKEN).build()

# هندلرهای ربات
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! من روی Webhook اجرا می‌شم.")

telegram_app.add_handler(CommandHandler("start", start))

@app.post(f"/webhook/{WEBHOOK_SECRET}")
async def telegram_webhook(request: Request):
    body = await request.body()
    await telegram_app.update_queue.put(Update.de_json(data=body.decode("utf-8"), bot=telegram_app.bot))
    return {"ok": True}

@app.on_event("startup")
async def on_startup():
    # ثبت Webhook در تلگرام
    webhook_url = f"{APP_URL}/webhook/{WEBHOOK_SECRET}"
    await telegram_app.bot.set_webhook(url=webhook_url)
