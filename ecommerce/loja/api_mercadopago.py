import mercadopago

public_key = "APP_USR-a1d95d2b-7351-41c5-882d-8bb7d44ea005"
token = "APP_USR-3511654696651487-021221-0d2c4937daae34616ca89531f40d2ad3-2264229261"

def criar_pagamento(itens_pedido, link):
    sdk = mercadopago.SDK(token)

    itens = []
    for item in itens_pedido:
        quantidade = int(item.quantidade)
        nome_produto = item.item_estoque.produto.nome
        preco_unitario = float(item.item_estoque.produto.preco)
        itens.append({
            "title": nome_produto,
            "quantity": quantidade,
            "unit_price": preco_unitario,
        })

    preference_data = {
        "items": itens,
        "auto_return": "all",
        "back_urls": {
            "success": link,
            "pending": link,
            "failure": link,
        }
    }

    resposta = sdk.preference().create(preference_data)

    print("DEBUG Mercado Pago:", resposta)  # <-- para veres a resposta real

    response_data = resposta.get("response", {})

    # tenta pegar o link de produção, senão usa o sandbox
    link_pagamento = response_data.get("init_point") or response_data.get("sandbox_init_point")

    if not link_pagamento:
        raise ValueError(f"Erro ao criar pagamento no Mercado Pago: {resposta}")

    id_pagamento = response_data.get("id")

    return link_pagamento, id_pagamento
