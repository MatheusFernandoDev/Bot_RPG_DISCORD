import random
import json
def escudo_merc():

    with open('bot/arquivos/json/escudos', 'r') as arquivo_json:
        dados_escudo = json.load(arquivo_json)
        
    escudo = random.choice(dados_escudo)

    return escudo

def armas_merc(maior):
    
    pericias = ["Treinamento com Armas Leves I", "Treinamento com Armas Pesadas I", "Treinamento com Armas de Haste I", "Treinamento com Armas de Contusão I", "Treinamento com Armas Longas I"]
    

    escolha = random.choice(pericias)
    

    # Armas Leves
    if (escolha == pericias[0]):

        # Abrindo o arquivo JSON
        with open('bot/arquivos/json/leves_atributos_dano.json', 'r') as arquivo_json:
            dados_armas = json.load(arquivo_json)

        if (maior == "atl"):
            arma = dados_armas[maior]
        else:
            arma = random.choice(dados_armas[maior])

        requisito_escudo = random.randint(1, 10)

        lista_equipamentos = {"Arma": arma}

    # Armas Pesadas
    elif (escolha ==  pericias[1]):
        
        # Abrindo o arquivo JSON
        with open('bot/arquivos/json/pesadas_atributos_dano.json', 'r') as arquivo_json:
            dados_armas = json.load(arquivo_json)
        
        arma = random.choice(dados_armas[maior])

        requisito_escudo = random.randint(1, 10)

        lista_equipamentos = {"Arma": arma}
    
    # Armas de haste
    elif (escolha ==  pericias[2]):

        # Abrindo o arquivo JSON
        with open('bot/arquivos/json/armas_haste.json', 'r') as arquivo_json:
            dados_armas = json.load(arquivo_json)
        
        tipo = random.choice(['arcos', 'bestas', 'balestra'])

        arma = random.choice(dados_armas[tipo])

        lista_equipamentos = {"Arma": arma}

    # Armas de Contusão
    elif (escolha == pericias[3]):

        # Abrindo o arquivo JSON
        with open('bot/arquivos/json/contusao_atributos_dano', 'r') as arquivo_json:
            dados_armas = json.load(arquivo_json)
        
        if (maior == "for"):

            arma = random.choice(dados_armas[maior])
        elif (maior == "atl"):
            arma = dados_armas[maior]
        else:
            arma = random.choice(dados_armas["for"])

        lista_equipamentos = {"Arma": arma}

    # Armas Longas
    else:

        # Abrindo o arquivo JSON
        with open('bot/arquivos/json/longas_atributos_dano', 'r') as arquivo_json:
            dados_armas = json.load(arquivo_json)
        
        arma = random.choice(dados_armas[maior])

        lista_equipamentos = {"Arma": arma}
    
    return  lista_equipamentos




