from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import requests
from amazon_ofertas import buscar_ofertas

TOKEN = "8304046291:AAE5obF01ZOo3Us6-bgatwbDBL5GJR8R4dE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot iniciado com sucesso!")

async def ofertas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = buscar_ofertas()
    await update.message.reply_text(texto)

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ofertas", ofertas))

    app.run_polling()

if __name__ == "__main__":
    main()
