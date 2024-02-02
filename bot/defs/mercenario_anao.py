import random
import pandas as pd
from defs.classes import prob_classes


nomes_nordicos = pd.read_csv("arquivos/nomes_nordicos.csv")
def merc_anao():
    nome = random.choice(nomes_nordicos['Personagem'])

    atributos1 = {"for": random.randint(1,8) + random.randint(1,3), "vig": random.randint(1,8), "des": random.randint(1,8) , "atl": random.randint(1,8), "eva": random.randint(1,8), "sab": random.randint(1,8) + random.randint(1,3), "arc": random.randint(1,8), "car": random.randint(1,8)}

    
    pc = sum(atributos1.values()) /40
        
       
    maior_valor = max((atributos1["vig"], atributos1["des"], atributos1["for"], atributos1["atl"], atributos1["eva"]))

    for chave, valor in atributos1.items():
        if valor == maior_valor:
            maior = chave
            break
        
    classe = prob_classes("Lanceiro", maior) 

    dados = {"Nome": nome, "PC": pc,"Classe": classe,"Atributos": atributos1} 
    return dados