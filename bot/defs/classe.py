
def prob_classes(preferencia, maior):
    
    """
        preferencial = classe de preferencia
        maior = maior atributo do personagem
    """
    
    import random
    
    classe = ""

    outras = {}

    classes = {"Sentinela": 0.15, "Ladino": 0.15, "Lanceiro": 0.15,"Cavaleiro": 0.15, "Rufião": 0.15}

    classes[preferencia] += 0.25

    if maior == "eva":
        classes["Ladino"] +=  0.05
        
        classe_bon = "Ladino"
        
    elif maior == "vig":
        classes["Cavaleiro"] +=  0.05

        classe_bon = "Cavaleiro"
    
    elif maior == "atl":
        classes["Rufião"] +=  0.05

        classe_bon = "Rufião"
    
    elif maior == "for":
        classes["Lanceiro"] +=  0.05
        
        classe_bon = "Lanceiro"

    elif maior == "des":
        classes["Sentinela"] +=  0.05

        classe_bon = "Sentinela" 
    
    for c in classes:
            if c != preferencia and c != classe_bon:
                classes[c] = 0.1375


    dado = random.randint(0, 100) / 100

    if dado <= classes[preferencia]:
        classe = preferencia
    
    elif dado <= classes[classe_bon] + classes[preferencia]:
        classe = classe_bon
    
    else:
        for c, v in classes.items():
            if c != preferencia and c != classe_bon:
                outras[c] = v
        classe = random.choice(list(outras.keys())) 

    return classe     
    
    






