import random
import json
def armas_merc():

    pesadas_atributos_dano = {"for": [
    {
        "nome": "Espada Curta",
        "dano": "1d4",
        "peso": "(3uP)",
        "tipo": "Afiado/Pesada (adaptável)",
        "requisito": 0,
        "habilidades": "20% FOR em dano. Arma de Soldado: com peso balanceado, sua arma tem fio em ambos os lados, podendo atacar subsequentemente com (+1) de iniciativa.",
        "durabilidade": "(7/7 dur.)",
        "slots": "(3/3 slots.)"
    },
    {
        "nome": "Espada de Liga Larga",
        "dano": "1d8",
        "peso": "(4uP)",
        "tipo": "Afiado/Pesado (adaptável)",
        "requisito": 10,
        "habilidades": "30% FOR em dano / -(2) em rolagem de iniciativa. + (0.2t) quando usando uma-mão.",
        "durabilidade": "(10/10 dur.)",
        "slots": "(3/3 slots.)"
    },
    {
        "nome": "Espada Montante",
        "dano": "1d6",
        "peso": "(3uP)",
        "tipo": "Afiado/Pesada",
        "requisito": 10,
        "habilidades": "30% FOR em dano - (1) de iniciativa. Alcance Leniente: é possível cobrir ataques em arco pela longitude (3 hexágonos frontais).",
        "durabilidade": "(10/10 dur.)",
        "slots": "(3/3 slots.)"
    },
    {
        "nome": "Falcata Tradicional",
        "dano": "1d5",
        "peso": "(3.5 uP)",
        "tipo": "Afiado/Pesado (adaptável)",
        "requisito": 0,
        "habilidades": "25% FOR em dano, - (2) iniciativa quando usando 1 mão, - (1) quando 2 mãos. Fio de Machado: quando cortando como um machado (horizontal) ganha bônus em choque em (1) ponto e quebra durabilidade com (+1).",
        "durabilidade": "(10/10 dur.)",
        "slots": "(3/3 slots.)"
    },
    {
        "nome": "ZWEIHANDERS: - Schwarkrieg",
        "dano": "1d6",
        "peso": "(5uP)",
        "tipo": "Afiado)",
        "requisito": 10,
        "habilidades": "20% ATL em dano, 10% FOR em dano / -(1) em rolagem de iniciativa. Guarda de Guerra: sua espada tem duas guardas, uma metálica e uma laminar, isso possibilita um bônus (+2) para desarmar quando se contesta um ataque ou (+1) quando aparando com a segunda guarda.",
        "durabilidade": "(10/10 dur.)",
        "slots": "(3/3 slots.)"
    },
    {
        "nome": "Flansdelân",
        "dano": "1d4",
        "peso": "(3uP)",
        "tipo": "Afiado/Leve",
        "requisito": 0,
        "habilidades": "10% EVA em dano 15% FOR em dano. / - (2) ATL. Par Sanguinário: sendo combinada com qualquer outra arma também equipada pode realizar ataques consecutivos substituindo o Desbalanço por Desvantagem",
        "durabilidade": "(4/4 dur.)",
        "slots": "(3/3 slots.)"
    },
    {
        "nome": "Cutelo de Batalha",
        "dano": "1d6",
        "peso": "(5uP)",
        "tipo": "Afiado/Pesado",
        "requisito": 0,
        "habilidades": "30% FOR em dano. / - (2) em rolagem de iniciativa. Corta-Partes: sua arma dá 1/3 do multiplicador adicional em todos os golpes",
        "durabilidade": "(9/9 dur.)",
        "slots": "(3/3 slots.)"
    },
    {
        "nome": "Nodachi-tachi",
        "dano": "1d6",
        "peso": "(4uP)",
        "tipo": "Afiado/Pesado",
        "requisito": 0,
        "habilidades": "30% FOR em dano – (-1) em iniciativa. (-1) EVA. Fio Leve ou Lâmina Dupla: lâminas duplas com pontas largas, sendo possível atacar de qualquer lado e deslizar até 50cm após atacar",
        "durabilidade": "(9/9 dur.)",
        "slots": "(3/3 slots.)"
    },
    {
        "nome": "Massugutana",
        "dano": "1d6",
        "peso": "(4uP)",
        "tipo": "Afiado/Pesado (adaptável)",
        "requisito": 0,
        "habilidades": "15% EVA e FOR em dano / (-3) DES / +(0.2)t em todos os movimentos físicos quando usando uma mão. Duelo Defensivo: é possível preparar-se para aparar ou guardar terreno com bônus (+2) logo após qualquer golpe realizado",
        "durabilidade": "(8/8 dur.)",
        "slots": "(3/3 slots.)"
    },
    {
        "nome": "Kentaraki",
        "dano": "1d5",
        "peso": "(3uP)",
        "tipo": "Afiado/Pesado",
        "requisito": 0,
        "habilidades": "20% FOR e 10% DES em dano - (-1) iniciativa. Fio Real: sua lâmina tem um gume com relevo, permitindo atacar subsequentemente sem entrar em Desbalanço (apenas 1 vez por ataque)",
        "durabilidade": "(8/8 dur.)",
        "slots": "(3/3 slots.)"
    },
    {
        "nome": "Katana Simples",
        "dano": "1d5",
        "peso": "(3uP)",
        "tipo": "Afiado/Pesadas (adaptável)",
        "requisito": 0,
        "habilidades": "10% FOR e DES em dano. Fio Leve: menor tempo para Cortes Transversais e menor tempo para Aparar",
        "durabilidade": "(7/7 dur.)",
        "slots": "(3/3 slots.)"
    },
    {
        "nome": "Machado Executor",
        "dano": "1d5",
        "peso": "(4uP)",
        "tipo": "Afiado/Pesado (adaptável)",
        "requisito": 0,
        "habilidades": "25% FOR – (-1) em rolagem de iniciativa / +(0.2t) quando usando uma-mão. Morte Dupla: esta arma tem dupla lâmina e gume, permitindo realizar um ataque giratório logo após um ataque horizontal sem dificuldade adicional ou desvantagem.",
        "durabilidade": "(10/10 dur.)",
        "slots": "(3/3 slots.)"
    },
    {
        "nome": "Machado Saxão",
        "dano": "1d6",
        "peso": "(5uP)",
        "tipo": "Afiado/Pesado",
        "requisito": 0,
        "habilidades": "20% FOR e 10% DES – (-1) em rolagem de iniciativa/ (-1) DES. Golpe Indômito: ataques dilaceram o alvo, causando (1d2x 0.5%) em multiplicador adicional por golpe perfeito.",
        "durabilidade": "(10/10 dur.)",
        "slots": "(3/3 slots.)"
    },
    {
        "nome": "Machado Crescente",
        "dano": "1d8",
        "peso": "(6uP)",
        "tipo": "Afiado/Pesado (adaptável)",
        "requisito": 10,
        "habilidades": "30% FOR em dano/ (-1) em ATL/ (-2) em rolagem de iniciativa/ rolar com desvantagem a Iniciativa quando usando 1 mão. Machadada Opressiva: exceto em ataques transversais essa arma fica presa no inimigo após o golpe drenando VIG à taxa de 115%.",
        "durabilidade": "(8/8 dur.)",
        "slots": "(3/3 slots.)"
    },
    {
        "nome": "Machado de Alça",
        "dano": "1d5",
        "peso": "(4uP)",
        "tipo": "Afiado/Pesado",
        "requisito": 0,
        "habilidades": "30% FOR em dano - (1) rolagens de iniciativa. Madeireira: pode usar para coleta sem prejuízo para durabilidade (+1 de prospecção) ou para batalha (-1 dur perdida).",
        "durabilidade": "(10/10 dur.)",
        "slots": "(3/3 slots.)"
    },
    {
        "nome": "Adaga-Barbatana",
        "dano": "1d4",
        "peso": "(4uP)",
        "tipo": "Afiado/Pesado (adaptável)",
        "requisito": 0,
        "habilidades": "10% DES em dano 10% FOR em dano. Barbatana de Lâmina: lâminas nas extremidades do cabo flexível e pode realizar ataques giratórios bonificados (+2).",
        "durabilidade": "(6/6 dur.)",
        "slots": "(3/3 slots.)"
    }
],"des":  [
    {
        "nome": "Rapieira de Bronze",
        "dano": "1d5",
        "peso": "(1,5 uP)",
        "tipo": "Afiado/Pesada",
        "requisito": 0,
        "habilidades": "20% DES em dano – (-1) em iniciativa. O Duelista: quando aparando uma lâmina, - 0.2t e não tem decréscimo de movimentação ao atacar.",
        "durabilidade": "(5/5 dur.)",
        "slots": "(3/3 slots)"
    },
    {
        "nome": "Iatagã",
        "dano": "1d6",
        "peso": "(2,5 uP)",
        "tipo": "(adaptável) Afiado/Pesado",
        "requisito": 0,
        "habilidades": "15% ATL e 15% DES em dano bônus, - (1) em iniciativa. +(0.2t) quando usando uma-mão. Lâmina Traiçoeira: estoca com +(20%) de dano.",
        "durabilidade": "(5/5 dur.)",
        "slots": "(3/3 slots)"
    },
    {
        "nome": "Katana Simples",
        "dano": "1d5",
        "peso": "(3uP)",
        "tipo": "Afiado/Pesadas (adaptável)",
        "requisito": 0,
        "habilidades": "10% FOR e DES em dano. Fio Leve: menor tempo para Cortes Transversais e menor tempo para Aparar",
        "durabilidade": "(7/7 dur.)",
        "slots": "(3/3 slots)"
    },
    {
        "nome": "Adaga-Barbatana",
        "dano": "1d4",
        "peso": "(4uP)",
        "tipo": "(adaptável) Afiado/Pesado",
        "requisito": 0,
        "habilidades": "10% DES em dano 10% FOR em dano. Barbatana de Lâmina: lâminas nas extremidades do cabo flexível e pode realizar ataques giratórios bonificados (+2).",
        "durabilidade": "(6/6 dur.)",
        "slots": "(3/3 slots)"
    }
], "atl": [
    {
        "nome": "Iatagã",
        "dano": "1d6",
        "peso": "(2,5 uP)",
        "tipo": "(adaptável) Afiado/Pesado",
        "requisito": 0,
        "habilidades": "15% ATL e 15% DES em dano bônus, - (1) em iniciativa. +(0.2t) quando usando uma-mão. Lâmina Traiçoeira: estoca com +(20%) de dano.",
        "durabilidade": "(5/5 dur.)",
        "slots": "(3/3 slots)"
    },
    {
        "nome": "Talwar",
        "dano": "1d6",
        "peso": "(2,5 uP)",
        "tipo": "(adaptável) Afiado/Pesado",
        "requisito": 0,
        "habilidades": "30% ATL em dano bônus, (-1) em iniciativa. +(0.2t) quando usando uma-mão. Lâmina Pesada: ataques verticais ganham bônus em colisão (+3)",
        "durabilidade": "(8/8 dur.)",
        "slots": "(3/3 slots)"
    },
    {
        "nome": "Surdaab",
        "dano": "1d6",
        "peso": "(3uP)",
        "tipo": "Afiado/Pesada (adaptável)",
        "requisito": 0,
        "habilidades": "15% EVA e ATL em dano / -(1) em rolagem de iniciativa. +(0.2)t em todos os movimentos físicos quando usando uma mão. Lâmina Lunar: sua arma tem apenas um gume, mas se acurva no bojo, facilitando tentativa de desarmar (+3) quando contestando em ataque consecutivo",
        "durabilidade": "(7/7 dur.)",
        "slots": "(3/3 slots)"
    }
],"eva": [
    {
        "nome": "Surdaab",
        "dano": "1d6",
        "peso": "(3uP)",
        "tipo": "Afiado/Pesada (adaptável)",
        "requisito": 0,
        "habilidades": "15% EVA e ATL em dano / -(1) em rolagem de iniciativa. +(0.2)t em todos os movimentos físicos quando usando uma mão. Lâmina Lunar: sua arma tem apenas um gume, mas se acurva no bojo, facilitando tentativa de desarmar (+3) quando contestando em ataque consecutivo",
        "durabilidade": "(7/7 dur.)",
        "slots": "(3/3 slots)"
    },
    {
        "nome": "Massugutana",
        "peso": "(4uP)",
        "dano": "(1d6)",
        "tipo": "Afiado/Pesado (adaptável)",
        "requisito": 0,
        "habilidades": "15% EVA e FOR em dano / (-3) DES / +(0.2)t em todos os movimentos físicos quando usando uma mão. Duelo Defensivo: é possível preparar-se para aparar ou guardar terreno com bônus (+2) logo após qualquer golpe realizado",
        "durabilidade": "(8/8 dur.)",
        "slots": "(3/3)"
    },
    {
        "nome": "Segadeira",
        "peso": "(4uP)",
        "dano": "(1d5)",
        "tipo": "Afiado/Pesado",
        "requisito": 0,
        "habilidades": "20% EVA em dano, 10% ATL em dano. -1 EVA. Cabeça Traiçoeira: sua arma pode aplicar até (2) tiques a mais de sangramento dependendo do dano causado (a partir de 25% VIG =1, mais de 50% = 2)).",
        "durabilidade": "(7/7)",
        "slots": "(3/3)"
    }
]}





    # with open('bot/arquivos/leves_atributos_dano.json', 'r') as arquivo_json:
    #     dados_armas = json.load(arquivo_json)

    # print(dados_armas)




    
    

armas_merc()