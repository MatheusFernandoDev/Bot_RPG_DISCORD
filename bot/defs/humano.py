import random
import pandas as pd
from defs.classe import prob_classes
from defs.arma import armas_merc
from defs.maior_valor_dic import chave_maior_valor

nomes = pd.read_csv("bot/arquivos/csv/nomes_rpg.csv")

def merc_humano():
    nome = random.choice(nomes['Personagem'])

    atributos1 = {"for": random.randint(1,8) + 1 , "des": random.randint(1,8) + 1, "atl": random.randint(1,8) + 1, "eva": random.randint(1,8) + 1, "vig": random.randint(1,8) + 1, "sab": random.randint(1,8) + 1, "arc": random.randint(1,8) + 1, "car": random.randint(1,8) + 1}

    
    pc = sum(atributos1.values()) /40
        
       
    maior_valor = chave_maior_valor(atributos1, "for", "des", "atl", "eva", "vig")

    maior_valor2 = chave_maior_valor(atributos1, "for", "des", "atl", "eva")
        
    classe = prob_classes("Lanceiro", maior_valor) 

    equipamento = armas_merc(maior_valor2)

    dados = {"Nome": nome, "PC": pc,"Classe": classe,"Atributos": atributos1, "Equipamento": equipamento}
    
    return dados

def player_humano():
    nome = random.choice(nomes['Personagem'])

    atributos = {"for": random.randint(1,10) + 1, "vig": random.randint(1,10) + 1, "des": random.randint(1,10) + 1, "atl": random.randint(1,10) + 1, "eva": random.randint(1,10) + 1, "sab": random.randint(1,10) + 1, "arc": random.randint(1,10) + 1, "car": random.randint(1,10) + 1}

    pc = sum(atributos.values()) /40

    dados = {"Nome": nome, "PC": pc,"Atributos": atributos} 
    
    return dados