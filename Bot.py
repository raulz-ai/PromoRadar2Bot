import requests
import time
import os

BOT_TOKEN = os.getenv("8304046291:AAE5obF01ZOo3Us6-bgatwbDBL5GJR8R4dE")
CHAT_ID = os.getenv("-1003394805895")

def enviar(texto):
    url = f"https://api.telegram.org/bot{8304046291:AAE5obF01ZOo3Us6-bgatwbDBL5GJR8R4dE}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": texto, "parse_mode": "HTML"}
    requests.post(url, data=data)

def main():
    while True:
        enviar("Bot está funcionando! 🔥")
        time.sleep(60)

main()
