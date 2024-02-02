import random

def escolha_armaduras():

    pesadatorço = ("Brúnea de Bronze do Cavaleiro (d. 15/15- AP) (5/5) slots – extremidades completas com ombreiras (- 3 EVA e -3 DES) 8uP.")

    mediastorço = ("Corselete de Malha (d. 7/7- AM) (4/4) slots. – todo Torso S. e I. (-1 DES); 6uP.")

    levetorço = ["Cota de Anéis (d. 8/8- AL) (4/4) slots – cobre Ombros e todo o Torso I. e S.; 4 uP.", 
                    "Colete de Couro e Peles (d. 5/5- AL) (3/3) slots – Torso S. e I., não protege Ombros; 3 uP."]

    armaduraspesadas = ["Elmo da Guarnição (d. 7/7 – AP) (4/4) slots. – Cabeça completa; visão e percepção reduzidos ((-3) na rolagem de auscultação e (-1) de modificador ocular); 2 uP.", 
        "Botas Metálicas (d. 8/8- AP) (2/2) slots – microrregiões dos pés até joelho; 2uP por pé; 1uP/pé", "Kilt de Bronze Simples (d. 12/12- AP) (3/3) slots – toda a parte inferior até os pés (-1 EVA); 4uP." ]        
            

    porcentagem = 0

    while porcentagem <= 69:

        porcentagem = random.randint(0, 100)
        if porcentagem >= 70 and porcentagem <= 79:
            protecao = (random.choice(levetorço))
            return protecao
        elif porcentagem >= 80 and porcentagem <= 89:
            protecao = mediastorço
            return protecao
        elif porcentagem >= 90 and porcentagem <= 94:
            protecao = pesadatorço
            return protecao
        else:
            protecao = pesadatorço
            protecao2 = random.choice(armaduraspesadas)

            protecao = protecao + "\n" + protecao2

            return protecao
        