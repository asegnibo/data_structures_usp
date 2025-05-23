def mochila_gulosa(capacidade, itens):
    itens.sort(key = lambda x: x.razao, reverse = True)
    capacidade_restante = capacidade
    itens_seleciondados = []
    for item in itens:
        if item.peso <= capacidade_restante:
            itens_seleciondados.append(item)
            capacidade_restante -= item.peso
    return itens_seleciondados

