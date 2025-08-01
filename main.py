import os
from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ["BOT_TOKEN"]

app = FastAPI()
bot_app = ApplicationBuilder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! ربات Webhook فعال و آماده است.")

bot_app.add_handler(CommandHandler("start", start))

@app.post("/webhook")
async def handle_webhook(req: Request):
    data = await req.json()
    update = Update.de_json(data, bot_app.bot)
    await bot_app.update_queue.put(update)
    return {"ok": True}
