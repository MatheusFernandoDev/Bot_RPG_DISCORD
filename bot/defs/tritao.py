import random
import pandas as pd
from defs.classe import prob_classes
from defs.arma import armas_merc
from defs.maior_valor_dic import chave_maior_valor

nomes_eslavos = pd.read_csv("bot/arquivos/csv/nomes_eslavos.csv")


def merc_tritao():
    nome = random.choice(nomes_eslavos['Personagem'])

    atributos1 = {"for": random.randint(1,8), "des": random.randint(1,8), "atl": random.randint(1,8)+ random.randint(1,3), "eva": random.randint(1,8), "vig": random.randint(1,8), "sab": random.randint(1,8), "arc": random.randint(1,8)+ random.randint(1,3), "car": random.randint(1,8)}

    
    pc = sum(atributos1.values()) /40
        
       
    maior_valor = chave_maior_valor(atributos1, "for", "des", "atl", "eva", "vig")

    maior_valor2 = chave_maior_valor(atributos1, "for", "des", "atl", "eva")
        
    classe = prob_classes("Rufião", maior_valor) 

    equipamento = armas_merc(maior_valor2)
    
    dados = {"Nome": nome, "PC": pc,"Classe": classe,"Atributos": atributos1, "Equipamento": equipamento}
     
    return dados

def player_tritao():
    nome = random.choice(nomes_eslavos['Personagem'])

    atributos = {"for": random.randint(1,10), "vig": random.randint(1,10) + random.randint(1,6), "des": random.randint(1,10), "atl": random.randint(1,10), "eva": random.randint(1,10), "sab": random.randint(1,10), "arc": random.randint(1,10) + random.randint(1,6), "car": random.randint(1,10)}

    pc = sum(atributos.values()) /40

    dados = {"Nome": nome, "PC": pc,"Atributos": atributos} 
    
    return dados