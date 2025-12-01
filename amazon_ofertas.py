import random

# Lista de produtos fixos só para exemplo (Amazon não tem API gratuita)
produtos = [
    {
        "nome": "Smartphone Samsung Galaxy A15",
        "preco": 789,
        "link": "https://www.amazon.com.br/dp/B0CRZ4SLR4?tag={TAG}"
    },
    {
        "nome": "Echo Dot 5ª Geração",
        "preco": 279,
        "link": "https://www.amazon.com.br/dp/B09B8V1L1N?tag={TAG}"
    },
    {
        "nome": "Fire TV Stick",
        "preco": 199,
        "link": "https://www.amazon.com.br/dp/B09B8TBCCS?tag={TAG}"
    }
]

def buscar_ofertas_amazon(tag):
    # Escolhe 1 produto aleatório
    produto = random.choice(produtos)

    # Adiciona o ID de afiliado ao link
    produto["link"] = produto["link"].replace("{TAG}", tag)

    return produto
