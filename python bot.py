import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 Welcome to d3vil Escrow Bot")

async def newdeal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        seller = context.args[0]
        amount = context.args[1]

        await update.message.reply_text(
            f"Deal created with {seller} for {amount} USDT"
        )
    except:
        await update.message.reply_text("Usage: /newdeal @seller amount")

async def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("newdeal", newdeal))

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
