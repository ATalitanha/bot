from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from fastapi import FastAPI
import uvicorn
import os

TOKEN = os.environ["BOT_TOKEN"]

app = FastAPI()

telegram_app = ApplicationBuilder().token(TOKEN).build()

@app.get("/")
async def root():
    return {"status": "Bot is running"}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! ربات فعاله و روی Render هست!")

telegram_app.add_handler(CommandHandler("start", start))
