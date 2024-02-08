import random
import pandas as pd
from defs.classes import prob_classes


nomes_amerindios = pd.read_csv("bot/arquivos/nomes_amerindios.csv")

def merc_tauru():
    nome = random.choice(nomes_amerindios['Personagem'])

    atributos1 = {"for": random.randint(1,8), "vig": random.randint(1,8) + random.randint(1,3), "des": random.randint(1,8), "atl": random.randint(1,8) + random.randint(1,3), "eva": random.randint(1,8), "sab": random.randint(1,8), "arc": random.randint(1,8), "car": random.randint(1,8)}

    
    pc = sum(atributos1.values()) /40
        
       
    maior_valor = max((atributos1["vig"], atributos1["des"], atributos1["for"], atributos1["atl"], atributos1["eva"]))

    for chave, valor in atributos1.items():
        if valor == maior_valor:
            maior = chave
            break
        
    classe = prob_classes("Lanceiro", maior) 

    dados = {"Nome": nome, "PC": pc,"Classe": classe,"Atributos": atributos1} 
    return dados

def player_tauru():
    nome = random.choice(nomes_amerindios['Personagem'])

    atributos = {"for": random.randint(1,10), "vig": random.randint(1,10) + random.randint(1,6), "des": random.randint(1,10), "atl": random.randint(1,10) + random.randint(1,6), "eva": random.randint(1,10 ), "sab": random.randint(1,10), "arc": random.randint(1,10), "car": random.randint(1,10)}

    pc = sum(atributos.values()) /40

    dados = {"Nome": nome, "PC": pc,"Atributos": atributos} 
    
    return dados