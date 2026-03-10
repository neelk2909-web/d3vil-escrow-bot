from telegram.ext import Updater, CommandHandler
import os

TOKEN = os.environ.get("BOT_TOKEN")

def start(update, context):
    update.message.reply_text("🔥 Welcome to d3vil Escrow Bot")

def help(update, context):
    update.message.reply_text(
        "Commands:\n/newdeal @seller amount"
    )

def newdeal(update, context):

    seller = context.args[0]
    amount = context.args[1]

    update.message.reply_text(
        f"Deal created with {seller} for {amount} USDT"
    )

updater = Updater(TOKEN, use_context=True)

dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", help))
dp.add_handler(CommandHandler("newdeal", newdeal))

updater.start_polling()
updater.idle()
