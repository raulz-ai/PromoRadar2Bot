import os
import time
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def enviar(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": msg,
        "parse_mode": "HTML"
    }
    requests.post(url, data=data)

def main():
    enviar("🚀 PromoRadar2Bot iniciou com sucesso!")
    while True:
        # manda só uma mensagem de teste por enquanto
        enviar("🔥 Bot rodando no Render!")
        time.sleep(60)

if __name__ == "__main__":
    main()
