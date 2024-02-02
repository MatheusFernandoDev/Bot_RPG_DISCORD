
import random
import pandas as pd
from defs.classes import prob_classes
from defs.mercenario_vamp import merc_vamp
from defs.mercenario_arque import merc_arque
from defs.mercenario_elfo import merc_elfo
from defs.mercenario_simio import merc_simio
from defs.mercenario_orc import merc_orc
from defs.mercenario_magma import merc_magma
from defs.mercenario_anao import merc_anao
from defs.mercenario_void  import merc_void
from defs.mercenario_troll import merc_troll
from defs.mercenario_lupin import merc_lupin
from defs.mercenario_taurus import merc_tauru
from defs.mercenario_lonine import merc_leonine
from defs.mercenario_feli import merc_felinio
from defs.mercenario_chacali import merc_chacalico
from defs.mercenario_javali  import merc_javalion
from defs.mercenario_reptilio import merc_reptilio
from defs.mercenario_ursarion import merc_ursa
from defs.proteção import escolha_armaduras
from defs.mercenario_denko import merc_denko
from defs.mercenario_aladico import merc_aladico
from defs.mercenario_nivolio import merc_nivolio
from defs.mercenario_humano import merc_humano
from discord.ext import commands
import discord

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)



@bot.event
async def on_ready():
    print(f"{bot.user} está online")

# Rolagem mercenario
@bot.command()
async def mercenario(ctx):

 
    racas = [
        "Vampirico", "Arqueonte", "Elfo", "Símio", "Orc", "Magmamir", "Anão", "Voidling", "Troll", "Lupínico","Taurus", "Leonine", "Felínio", "Chacálico", "Javálion", "Reptilio", "Ursárion","Denkomu", "Aládico", "Nivólio", "Humano"
        ]
    
    
    
    raç = random.choice(racas)
    

    if raç == "Vampirico":
        dados = merc_vamp()  
    elif raç == "Arqueonte":
        dados = merc_arque()
    elif raç == "Elfo":
        dados = merc_elfo() 
    elif raç == "Símio":
        dados = merc_simio()   
    elif raç == "Orc":
        dados = merc_orc()
    elif raç == "Magmamir":
        dados = merc_magma()
    elif raç == "Anão":
        dados = merc_anao()
    elif raç == "Voidling":
        dados = merc_void()
    elif raç == "Troll":
        dados = merc_troll()
    elif raç == "Lupínico": 
        dados = merc_lupin()
    elif raç == "Taurus":
        dados = merc_tauru()
    elif raç == "Leonine":
        dados = merc_leonine()  
    elif raç == "Felínio":
        dados = merc_felinio()
    elif raç == "Chacálico":
        dados = merc_chacalico()
    elif raç == "Javálion":
        dados = merc_javalion()
    elif raç == "Reptilio":
        dados = merc_reptilio()
    elif raç == "Ursárion":
        dados = merc_ursa()
    elif raç == "Denkomu":
        dados = merc_denko()
    elif raç == "Aládico":
        dados = merc_aladico()
    elif raç == "Nivólio":
        dados = merc_nivolio()
    else:
        dados = merc_humano()
    
    channel = (ctx.channel)
    
    await ctx.message.delete()
    

    await channel.send(f'{ctx.author.mention} \nNome: {dados["Nome"]:<10} Raça: {raç:<10} PC: {dados["PC"]}  Classe:  {dados["Classe"]}\n'
      f"ARC: {dados['Atributos']['arc']:<4}  VIG: {dados['Atributos']['vig']:<4} DES: {dados['Atributos']['des']:<4} SAB: {dados['Atributos']['sab']:<4}\n"
      f"FOR: {dados['Atributos']['for']:<4} ATL: {dados['Atributos']['atl']:<4} EVA: {dados['Atributos']['eva']:<4} CAR: {dados['Atributos']['car']:<4}\n"
      f"\nProteção: \n{escolha_armaduras():<4}")
    
       
#  Rolagem Vampirico
@bot.command()
async def vampirico(ctx):   
    
    
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10) + random.randint(1, 6)
    vig = random.randint(1,10)
    des = random.randint(1,10)
    sab = random.randint(1,10)
    forç = random.randint(1,10) + random.randint(1, 6)
    atl = random.randint(1,10)
    eva = random.randint(1,10)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()

    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Vampirico   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Arqueonte
@bot.command()
async def arqueonte(ctx):   

    channel = (ctx.channel)    
    
    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10)
    vig = random.randint(1,10)
    des = random.randint(1,10)
    sab = random.randint(1,10) + random.randint(1, 6) + random.randint(1, 6)
    forç = random.randint(1,10)
    atl = random.randint(1,10)
    eva = random.randint(1,10)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Arqueonte   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Elfo
@bot.command()
async def elfo(ctx):   
    
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10)
    vig = random.randint(1,10)
    des = random.randint(1,10) + random.randint(1, 6)
    sab = random.randint(1,10) + random.randint(1, 6)
    forç = random.randint(1,10)
    atl = random.randint(1,10)
    eva = random.randint(1,10)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()

    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Elfo   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Simio
@bot.command()
async def simio(ctx):   
    
    
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10)
    vig = random.randint(1,10)
    des = random.randint(1,10) + random.randint(1, 6)
    sab = random.randint(1,10)
    forç = random.randint(1,10) + random.randint(1, 6)
    atl = random.randint(1,10)
    eva = random.randint(1,10)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Símio   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Orc
@bot.command()
async def orc(ctx):   
   
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10)
    vig = random.randint(1,10) + random.randint(1, 6)
    des = random.randint(1,10)
    sab = random.randint(1,10)
    forç = random.randint(1,10) + random.randint(1, 6)
    atl = random.randint(1,10)
    eva = random.randint(1,10)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Orc   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Magmamir
@bot.command()
async def magmamir(ctx):   
    
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10) + random.randint(1, 6)
    vig = random.randint(1,10) + random.randint(1, 6)
    des = random.randint(1,10)
    sab = random.randint(1,10)
    forç = random.randint(1,10)
    atl = random.randint(1,10)
    eva = random.randint(1,10)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Magmamir   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Anão
@bot.command()
async def anao(ctx):
    
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10)
    vig = random.randint(1,10)
    des = random.randint(1,10)
    sab = random.randint(1,10) + random.randint(1, 6)
    forç = random.randint(1,10) + random.randint(1, 6)
    atl = random.randint(1,10)
    eva = random.randint(1,10)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Anão   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

#  Rolagem Voidling
@bot.command()
async def voidling(ctx):   
   
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10)
    vig = random.randint(1,10)
    des = random.randint(1,10) + random.randint(1, 6)
    sab = random.randint(1,10)
    forç = random.randint(1,10)
    atl = random.randint(1,10)
    eva = random.randint(1,10) + random.randint(1, 6)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Voidling   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Troll
@bot.command()
async def troll(ctx):   

    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10) + random.randint(1, 6) + random.randint(1, 6)
    vig = random.randint(1,10)
    des = random.randint(1,10)
    sab = random.randint(1,10)
    forç = random.randint(1,10)
    atl = random.randint(1,10)
    eva = random.randint(1,10)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Troll   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Lupínico
@bot.command()
async def lupinico(ctx):   

    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10)
    vig = random.randint(1,10)
    des = random.randint(1,10)
    sab = random.randint(1,10)
    forç = random.randint(1,10)
    atl = random.randint(1,10) + random.randint(1, 6)
    eva = random.randint(1,10) + random.randint(1, 6)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Lupínico   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

#Rolagem Taurus
@bot.command()
async def taurus(ctx):   
   
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10)
    vig = random.randint(1,10) + random.randint(1, 6)
    des = random.randint(1,10)
    sab = random.randint(1,10)
    forç = random.randint(1,10)
    atl = random.randint(1,10) + random.randint(1, 6)
    eva = random.randint(1,10)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Taurus   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Leonine
@bot.command()
async def leonine(ctx):   
    
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10)
    vig = random.randint(1,10)
    des = random.randint(1,10)
    sab = random.randint(1,10)
    forç = random.randint(1,10) + random.randint(1, 6)
    atl = random.randint(1,10) + random.randint(1, 6)
    eva = random.randint(1,10)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Leonine   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Felínio
@bot.command()
async def felinio(ctx):   
    
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10)
    vig = random.randint(1,10)
    des = random.randint(1,10) + random.randint(1, 6) + random.randint(1, 6)
    sab = random.randint(1,10) 
    forç = random.randint(1,10)
    atl = random.randint(1,10)
    eva = random.randint(1,10)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Felínio   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Chacálico
@bot.command()
async def chacalico(ctx):   
    
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10)
    vig = random.randint(1,10)
    des = random.randint(1,10)
    sab = random.randint(1,10)
    forç = random.randint(1,10) + random.randint(1, 6)
    atl = random.randint(1,10)
    eva = random.randint(1,10) + random.randint(1, 6)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Chacálico   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Javálion
@bot.command()
async def javalion(ctx):   
    
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10)
    vig = random.randint(1,10) + random.randint(1, 6) + random.randint(1, 6)
    des = random.randint(1,10)
    sab = random.randint(1,10)
    forç = random.randint(1,10)
    atl = random.randint(1,10)
    eva = random.randint(1,10)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Javálion   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Reptilio
@bot.command()
async def reptilio(ctx):   
    
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10)
    vig = random.randint(1,10)
    des = random.randint(1,10)
    sab = random.randint(1,10)
    forç = random.randint(1,10)
    atl = random.randint(1,10)
    eva = random.randint(1,10) + random.randint(1, 6) + random.randint(1, 6)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Repitilio   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Ursárion
@bot.command()
async def ursarion(ctx):   
    
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10)
    vig = random.randint(1,10)
    des = random.randint(1,10)
    sab = random.randint(1,10)
    forç = random.randint(1,10) + random.randint(1, 6) + random.randint(1, 6)
    atl = random.randint(1,10)
    eva = random.randint(1,10)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()    
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Ursarion   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Tritão
@bot.command()
async def tritao(ctx):   
    
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10) + random.randint(1, 6)
    vig = random.randint(1,10)
    des = random.randint(1,10)
    sab = random.randint(1,10)
    forç = random.randint(1,10)
    atl = random.randint(1,10) + random.randint(1, 6)
    eva = random.randint(1,10)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Tritão   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Denkomu
@bot.command()
async def denkomu(ctx):   
    
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10)
    vig = random.randint(1,10) + random.randint(1, 6)
    des = random.randint(1,10) + random.randint(1, 6)
    sab = random.randint(1,10)
    forç = random.randint(1,10)
    atl = random.randint(1,10)
    eva = random.randint(1,10)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Denkomu   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Aládico
@bot.command()
async def aladico(ctx):   
   
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10)
    vig = random.randint(1,10)
    des = random.randint(1,10)
    sab = random.randint(1,10)
    forç = random.randint(1,10)
    atl = random.randint(1,10) + random.randint(1, 6) + random.randint(1, 6)
    eva = random.randint(1,10)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Aládico   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Nivólio
@bot.command()
async def nivolio(ctx):   
    
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10) + random.randint(1, 6)
    vig = random.randint(1,10)
    des = random.randint(1,10)
    sab = random.randint(1,10)
    forç = random.randint(1,10)
    atl = random.randint(1,10)
    eva = random.randint(1,10) + random.randint(1, 6)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Arqueonte   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Humano
@bot.command()
async def humano(ctx):   
    
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10) + 1
    vig = random.randint(1,10) + 1
    des = random.randint(1,10) + 1
    sab = random.randint(1,10) + 1
    forç = random.randint(1,10) + 1
    atl = random.randint(1,10) + 1
    eva = random.randint(1,10) + 1
    car = random.randint(1,10) + 1

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Humano   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

bot.run("MTEzMDE1OTEwMTIyMjA2MDExMg.GxrsPV.mfI-GfJqsQlrTqcDpZtGHxaUO2hWROVZAsxd-I")