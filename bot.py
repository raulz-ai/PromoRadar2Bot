import os
import time
import requests
from amazon_ofertas import buscar_ofertas_amazon

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
AFILIADO = "promoradar0cb-20"  # seu ID fixo

def enviar(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": msg, "parse_mode": "HTML"}
    requests.post(url, data=data)

def main():
    enviar("🤖 PromoRadar2Bot Iniciado!")

    while True:
        ofertas = buscar_ofertas_amazon("smartphone", AFILIADO)

        if not ofertas:
            enviar("⚠️ Nenhuma oferta encontrada na Amazon agora.")
        else:
            for o in ofertas[:3]:  # manda até 3 promoções por loop
                mensagem = f"""
📦 <b>{o['nome']}</b>
💰 Preço: R$ {o['preco']}
🏬 Loja: {o['loja']}
🔗 <a href="{o['link']}">Comprar com desconto</a>
"""
                enviar(mensagem)

        time.sleep(1800)  # roda a cada 30 minutos

if __name__ == "__main__":
    main()
