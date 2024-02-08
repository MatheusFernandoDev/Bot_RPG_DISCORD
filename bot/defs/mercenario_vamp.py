import random
import pandas as pd
from defs.classes import prob_classes




nomes_alemaes = pd.read_csv("bot/arquivos/nomes_alemaes.csv")

def merc_vamp():
    
        nome = random.choice(nomes_alemaes['Personagem'])

        atributos = {"for": random.randint(1,8) + random.randint(1,3), "vig": random.randint(1,8), "des": random.randint(1,8), "atl": random.randint(1,8), "eva": random.randint(1,8), "sab": random.randint(1,8), "arc": random.randint(1,8) + random.randint(1,3), "car": random.randint(1,8)}

    
        pc = sum(atributos.values()) /40
        
       
        maior_valor = max((atributos["vig"], atributos["des"], atributos["for"], atributos["atl"], atributos["eva"]))

        for chave, valor in atributos.items():
            if valor == maior_valor:
                maior = chave
                break
        
        classe = prob_classes("Cavaleiro", maior)
        
        dados = {"Nome": nome, "PC": pc,"Classe": classe,"Atributos": atributos} 
        return dados
        
def player_vamp():
    nome = random.choice(nomes_alemaes['Personagem'])

    atributos = {"for": random.randint(1,10) + random.randint(1,6), "vig": random.randint(1,10), "des": random.randint(1,10), "atl": random.randint(1,10), "eva": random.randint(1,10), "sab": random.randint(1,10), "arc": random.randint(1,10) + random.randint(1,6), "car": random.randint(1,10)}

    pc = sum(atributos.values()) /40

    dados = {"Nome": nome, "PC": pc,"Atributos": atributos} 
    
    return dados