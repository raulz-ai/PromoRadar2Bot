import requests
from bs4 import BeautifulSoup

AFFILIATE_TAG = "promoradar0cb-20"  # seu link de afiliado da Amazon

def buscar_ofertas():
    url = "https://www.amazon.com.br/gp/goldbox"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept-Language": "pt-BR,pt;q=0.9",
    }

    try:
        r = requests.get(url, headers=headers, timeout=10)
    except:
        return "⚠️ Erro ao acessar a Amazon. Tente novamente."

    soup = BeautifulSoup(r.text, "html.parser")

    # Seleção dos cards reais da página da Amazon
    cards = soup.select("div.DealCard-module__dealCard_1H0Lh")

    if not cards:
        return "⚠️ Não foi possível carregar as ofertas hoje."

    texto = "🔥 *Ofertas do dia da Amazon* 🔥\n\n"

    for card in cards[:5]:
        titulo = card.select_one("span.DealCard-module__truncate_3v4MM")
        link = card.find("a", href=True
