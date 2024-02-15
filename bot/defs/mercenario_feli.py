import random
import pandas as pd
from defs.classes import prob_classes
from defs.armas import armas_merc

nomes_chineses = pd.read_csv("bot/arquivos/csv/nomes_chineses.csv")


def merc_felinio():
    nome = random.choice(nomes_chineses['Personagem'])

    atributos1 = {"for": random.randint(1,8), "vig": random.randint(1,8), "des": random.randint(1,8) + random.randint(1,3)  + random.randint(1,3), "atl": random.randint(1,8), "eva": random.randint(1,8), "sab": random.randint(1,8), "arc": random.randint(1,8), "car": random.randint(1,8)}

    
    pc = sum(atributos1.values()) /40
        
       
    maior_valor = max((atributos1["vig"], atributos1["des"], atributos1["for"], atributos1["atl"], atributos1["eva"]))

    maior_valor2 = max((atributos1["des"], atributos1["for"], atributos1["atl"], atributos1["eva"]))

    for chave, valor in atributos1.items():
        for chave, valor in atributos1.items():
            if valor == maior_valor:
                maior = chave
                break         
        if valor == maior_valor2:
                maior_arma = chave
                break
        
    classe = prob_classes("Ladino", maior) 

    equipamento = armas_merc(maior_arma)

    dados = {"Nome": nome, "PC": pc,"Classe": classe,"Atributos": atributos1, "Equipamento": equipamento}
     
    return dados

def player_felinio():
    nome = random.choice(nomes_chineses['Personagem'])

    atributos = {"for": random.randint(1,10), "vig": random.randint(1,10), "des": random.randint(1,10) + random.randint(1,6) + random.randint(1,6), "atl": random.randint(1,10), "eva": random.randint(1,10), "sab": random.randint(1,10), "arc": random.randint(1,10), "car": random.randint(1,10)}

    pc = sum(atributos.values()) /40

    dados = {"Nome": nome, "PC": pc,"Atributos": atributos} 
    
    return dados