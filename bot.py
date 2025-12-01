import os
from telegram import Bot
from amazon_ofertas import buscar_ofertas_amazon

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
AMAZON_TAG = os.getenv("AMAZON_TAG")

bot = Bot(TOKEN)

def main():
    oferta = buscar_ofertas_amazon(AMAZON_TAG)

    mensagem = (
        f"🔥 *Oferta do dia!*\n\n"
        f"📱 *{oferta['nome']}*\n"
        f"💸 Preço: R${oferta['preco']}\n\n"
        f"👉 Link: {oferta['link']}"
    )

    bot.send_message(CHAT_ID, mensagem, parse_mode="Markdown")

if __name__ == "__main__":
    main()
