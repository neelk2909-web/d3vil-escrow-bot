import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

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

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("newdeal", newdeal))

app.run_polling()
