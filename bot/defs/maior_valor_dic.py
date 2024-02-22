def chave_maior_valor(dicionario, *chaves):
    valores = [dicionario[chave] for chave in chaves]
    max_valor = max(valores)
    return chaves[valores.index(max_valor)]