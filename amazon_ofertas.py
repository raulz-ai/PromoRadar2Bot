import requests

def buscar_ofertas_amazon(termo_busca, afiliado_id):
    url = f"https://api.buscape.com.br/services/search/?q={termo_busca}"
    resp = requests.get(url, timeout=5)

    if resp.status_code != 200:
        return []

    dados = resp.json()
    resultados = []

    for item in dados.get("products", []):
        for offer in item.get("offers", []):
            loja = offer.get("source")
            link = offer.get("offer_url")

            # filtrar ofertas da Amazon
            if loja and "amazon" in loja.lower():
                # adicionar link de afiliado
                link_afiliado = f"{link}?tag={afiliado_id}"

                resultados.append({
                    "nome": item.get("product_name"),
                    "preco": offer.get("price"),
                    "loja": loja,
                    "link": link_afiliado,
                    "imagem": item.get("product_images", [None])[0]
                })

    return resultados
