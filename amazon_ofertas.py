import requests
from bs4 import BeautifulSoup

AFFILIATE_TAG = "raulz07-20"  # <-- seu link de afiliado aqui

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

    # Cards de ofertas
    cards = soup.select("div.DealCard-module__dealCard_1H0Lh")

    if not cards:
        return "⚠️ Não foi possível carregar as ofertas hoje."

    texto = "🔥 *Ofertas do dia da Amazon* 🔥\n\n"

    for card in cards[:5]:
        titulo = card.select_one("span.DealCard-module__truncate_3v4MM")
        link = card.find("a", href=True)

        if not titulo or not link:
            continue

        nome = titulo.get_text(strip=True)
        url_prod = "https://www.amazon.com.br" + link["href"]

        # adiciona tag de afiliado automaticamente
        if "tag=" not in url_prod:
            separador = "&" if "?" in url_prod else "?"
            url_prod += f"{separador}tag={AFFILIATE_TAG}"

        texto += f"• {nome}\n{url_prod}\n\n"

    return texto
