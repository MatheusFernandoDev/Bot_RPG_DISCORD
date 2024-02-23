import random
import pandas as pd
from defs.classe import prob_classes
from defs.arma import armas_merc
from defs.maior_valor_dic import chave_maior_valor
from defs.atributos import rolagem_atributos

nomes_italo_continental = pd.read_csv("bot/arquivos/csv/nomes_italo_continental.csv")

def merc_void():
    nome = random.choice(nomes_italo_continental['Personagem'])

    atributos1 = rolagem_atributos(8, 3, "eva", "des")

    
    pc = sum(atributos1.values()) /40
        
       
    maior_valor = chave_maior_valor(atributos1, "for", "des", "atl", "eva", "vig")

    maior_valor2 = chave_maior_valor(atributos1, "for", "des", "atl", "eva")
        
    classe = prob_classes("Ladino", maior_valor)

    equipamento = armas_merc(maior_valor2)

    dados = {"Nome": nome, "PC": pc,"Classe": classe,"Atributos": atributos1, "Equipamento": equipamento}
     
    return dados

def player_void():
    nome = random.choice(nomes_italo_continental['Personagem'])

    atributos = rolagem_atributos(10, 6, "eva", "des")

    pc = sum(atributos.values()) /40

    dados = {"Nome": nome, "PC": pc,"Atributos": atributos} 
    
    return dados