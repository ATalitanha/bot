import os
from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import ApplicationBuilder

TOKEN = os.environ["BOT_TOKEN"]

app = FastAPI()
bot_app = ApplicationBuilder().token(TOKEN).build()

@app.post("/webhook")
async def handle_webhook(req: Request):
    data = await req.json()
    update = Update.de_json(data, bot_app.bot)
    await bot_app.update_queue.put(update)
    return {"ok": True}
