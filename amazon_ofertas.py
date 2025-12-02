import requests
from bs4 import BeautifulSoup

def buscar_ofertas():
    url = "https://www.amazon.com.br/gp/goldbox"
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(r.text, "html.parser")

    ofertas = soup.select(".a-section.a-text-center")
    texto = "🔥 Ofertas do dia:\n\n"

    for o in ofertas[:5]:
        titulo = o.get_text(strip=True)
        if titulo:
            texto += f"- {titulo}\n"

    return texto
