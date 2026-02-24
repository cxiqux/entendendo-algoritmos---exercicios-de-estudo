def procure_pela_chave(caixa_principal):
    pilha = [caixa_principal]  

    while pilha:               
        caixa = pilha.pop()

        for item in caixa:
            if isinstance(item, list):
                pilha.append(item)
            elif item == "chave":
                print("achei a chave!")
                return True

    return False

caixa = [
    ["papel", "moeda"],
    ["livro", ["controle", "chave"]],
    "copo"
]

procure_pela_chave(caixa)