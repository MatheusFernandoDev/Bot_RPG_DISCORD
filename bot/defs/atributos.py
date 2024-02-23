import random

def rolagem_atributos(rolagem, rolagem2, atributo1, atributo2):
    
    atributos = {"for": random.randint(1,rolagem), 
                 "des": random.randint(1,rolagem), 
                 "atl": random.randint(1,rolagem), 
                 "eva": random.randint(1,rolagem), 
                 "vig": random.randint(1,rolagem), 
                 "sab": random.randint(1,rolagem), 
                 "arc": random.randint(1,rolagem),  
                 "car": random.randint(1,rolagem)
                }
    
    atributos[atributo1] += random.randint(1,rolagem2)
    atributos[atributo2] += random.randint(1,rolagem2)

    return atributos