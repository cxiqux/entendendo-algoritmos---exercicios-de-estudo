def procure_pela_chave(caixa):
    for item in caixa:
        if isinstance(item, list):
            if procure_pela_chave(item):
                return True
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