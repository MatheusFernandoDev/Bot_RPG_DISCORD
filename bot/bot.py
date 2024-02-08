
import random
import pandas as pd
from defs.classes import prob_classes
from defs.mercenario_vamp import merc_vamp, player_vamp
from defs.mercenario_arque import merc_arque, player_arque
from defs.mercenario_elfo import merc_elfo, player_elfo
from defs.mercenario_simio import merc_simio, player_simio
from defs.mercenario_orc import merc_orc, player_orc
from defs.mercenario_magma import merc_magma, player_magma
from defs.mercenario_anao import merc_anao, player_anao
from defs.mercenario_void  import merc_void, player_void
from defs.mercenario_troll import merc_troll, player_troll
from defs.mercenario_lupin import merc_lupin, player_lupin
from defs.mercenario_taurus import merc_tauru, player_tauru
from defs.mercenario_lonine import merc_leonine, player_leonine
from defs.mercenario_feli import merc_felinio, player_felinio
from defs.mercenario_chacali import merc_chacalico, player_chacalico
from defs.mercenario_javali  import merc_javalion, player_javalion
from defs.mercenario_reptilio import merc_reptilio, player_reptilio
from defs.mercenario_ursarion import merc_ursa, player_ursa
from defs.mercenario_tritao import merc_tritao, player_tritao
from defs.mercenario_denko import merc_denko, player_denko
from defs.mercenario_aladico import merc_aladico, player_aladico
from defs.mercenario_nivolio import merc_nivolio, player_nivolio
from defs.mercenario_humano import merc_humano, player_humano
from defs.proteção import escolha_armaduras
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

    dados = player_vamp()

    await ctx.message.delete()

    await channel.send(f'{ctx.author.mention} \nNome: {dados["Nome"]:<10} Raça: {"Vampirico":<10} PC: {dados["PC"]}\n'
      f"ARC: {dados['Atributos']['arc']:<4}  VIG: {dados['Atributos']['vig']:<4} DES: {dados['Atributos']['des']:<4} SAB: {dados['Atributos']['sab']:<4}\n"
      f"FOR: {dados['Atributos']['for']:<4} ATL: {dados['Atributos']['atl']:<4} EVA: {dados['Atributos']['eva']:<4} CAR: {dados['Atributos']['car']:<4}")

# Rolagem Arqueonte
@bot.command()
async def arqueonte(ctx):   

    channel = (ctx.channel)    
    
    dados = player_arque()

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention} \nNome: {dados["Nome"]:<10} Raça: {"Arqueonte":<10} PC: {dados["PC"]}\n'
      f"ARC: {dados['Atributos']['arc']:<4}  VIG: {dados['Atributos']['vig']:<4} DES: {dados['Atributos']['des']:<4} SAB: {dados['Atributos']['sab']:<4}\n"
      f"FOR: {dados['Atributos']['for']:<4} ATL: {dados['Atributos']['atl']:<4} EVA: {dados['Atributos']['eva']:<4} CAR: {dados['Atributos']['car']:<4}")

# Rolagem Elfo
@bot.command()
async def elfo(ctx):   
    
    channel = (ctx.channel)

    dados = player_elfo()

    await ctx.message.delete()

    await channel.send(f'{ctx.author.mention} \nNome: {dados["Nome"]:<10} Raça: {"Elfo":<10} PC: {dados["PC"]}\n'
      f"ARC: {dados['Atributos']['arc']:<4}  VIG: {dados['Atributos']['vig']:<4} DES: {dados['Atributos']['des']:<4} SAB: {dados['Atributos']['sab']:<4}\n"
      f"FOR: {dados['Atributos']['for']:<4} ATL: {dados['Atributos']['atl']:<4} EVA: {dados['Atributos']['eva']:<4} CAR: {dados['Atributos']['car']:<4}")
# Rolagem Simio
@bot.command()
async def simio(ctx):   
    
    
    channel = (ctx.channel)


    dados = player_simio()

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention} \nNome: {dados["Nome"]:<10} Raça: {"Simio":<10} PC: {dados["PC"]}\n'
      f"ARC: {dados['Atributos']['arc']:<4}  VIG: {dados['Atributos']['vig']:<4} DES: {dados['Atributos']['des']:<4} SAB: {dados['Atributos']['sab']:<4}\n"
      f"FOR: {dados['Atributos']['for']:<4} ATL: {dados['Atributos']['atl']:<4} EVA: {dados['Atributos']['eva']:<4} CAR: {dados['Atributos']['car']:<4}")

# Rolagem Orc
@bot.command()
async def orc(ctx):   
   
    channel = (ctx.channel)

    dados = player_orc()

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention} \nNome: {dados["Nome"]:<10} Raça: {"Orc":<10} PC: {dados["PC"]}\n'
      f"ARC: {dados['Atributos']['arc']:<4}  VIG: {dados['Atributos']['vig']:<4} DES: {dados['Atributos']['des']:<4} SAB: {dados['Atributos']['sab']:<4}\n"
      f"FOR: {dados['Atributos']['for']:<4} ATL: {dados['Atributos']['atl']:<4} EVA: {dados['Atributos']['eva']:<4} CAR: {dados['Atributos']['car']:<4}")

# Rolagem Magmamir
@bot.command()
async def magmamir(ctx):   
    
    channel = (ctx.channel)

    dados = player_magma()

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention} \nNome: {dados["Nome"]:<10} Raça: {"Magmamir":<10} PC: {dados["PC"]}\n'
      f"ARC: {dados['Atributos']['arc']:<4}  VIG: {dados['Atributos']['vig']:<4} DES: {dados['Atributos']['des']:<4} SAB: {dados['Atributos']['sab']:<4}\n"
      f"FOR: {dados['Atributos']['for']:<4} ATL: {dados['Atributos']['atl']:<4} EVA: {dados['Atributos']['eva']:<4} CAR: {dados['Atributos']['car']:<4}")

# Rolagem Anão
@bot.command()
async def anao(ctx):
    
    channel = (ctx.channel)

    dados = player_anao()

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention} \nNome: {dados["Nome"]:<10} Raça: {"Anão":<10} PC: {dados["PC"]}\n'
      f"ARC: {dados['Atributos']['arc']:<4}  VIG: {dados['Atributos']['vig']:<4} DES: {dados['Atributos']['des']:<4} SAB: {dados['Atributos']['sab']:<4}\n"
      f"FOR: {dados['Atributos']['for']:<4} ATL: {dados['Atributos']['atl']:<4} EVA: {dados['Atributos']['eva']:<4} CAR: {dados['Atributos']['car']:<4}")

#  Rolagem Voidling
@bot.command()
async def voidling(ctx):   
   
    channel = (ctx.channel)

    dados = player_void()

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention} \nNome: {dados["Nome"]:<10} Raça: {"Voidling":<10} PC: {dados["PC"]}\n'
      f"ARC: {dados['Atributos']['arc']:<4}  VIG: {dados['Atributos']['vig']:<4} DES: {dados['Atributos']['des']:<4} SAB: {dados['Atributos']['sab']:<4}\n"
      f"FOR: {dados['Atributos']['for']:<4} ATL: {dados['Atributos']['atl']:<4} EVA: {dados['Atributos']['eva']:<4} CAR: {dados['Atributos']['car']:<4}")

# Rolagem Troll
@bot.command()
async def troll(ctx):   

    channel = (ctx.channel)

    dados = player_troll()

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention} \nNome: {dados["Nome"]:<10} Raça: {"Troll":<10} PC: {dados["PC"]}\n'
      f"ARC: {dados['Atributos']['arc']:<4}  VIG: {dados['Atributos']['vig']:<4} DES: {dados['Atributos']['des']:<4} SAB: {dados['Atributos']['sab']:<4}\n"
      f"FOR: {dados['Atributos']['for']:<4} ATL: {dados['Atributos']['atl']:<4} EVA: {dados['Atributos']['eva']:<4} CAR: {dados['Atributos']['car']:<4}")

# Rolagem Lupínico
@bot.command()
async def lupinico(ctx):   

    channel = (ctx.channel)

    dados = player_lupin()

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention} \nNome: {dados["Nome"]:<10} Raça: {"Lupinico":<10} PC: {dados["PC"]}\n'
      f"ARC: {dados['Atributos']['arc']:<4}  VIG: {dados['Atributos']['vig']:<4} DES: {dados['Atributos']['des']:<4} SAB: {dados['Atributos']['sab']:<4}\n"
      f"FOR: {dados['Atributos']['for']:<4} ATL: {dados['Atributos']['atl']:<4} EVA: {dados['Atributos']['eva']:<4} CAR: {dados['Atributos']['car']:<4}")

#Rolagem Taurus
@bot.command()
async def taurus(ctx):   
   
    channel = (ctx.channel)

    dados = player_tauru()

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention} \nNome: {dados["Nome"]:<10} Raça: {"Taurus":<10} PC: {dados["PC"]}\n'
      f"ARC: {dados['Atributos']['arc']:<4}  VIG: {dados['Atributos']['vig']:<4} DES: {dados['Atributos']['des']:<4} SAB: {dados['Atributos']['sab']:<4}\n"
      f"FOR: {dados['Atributos']['for']:<4} ATL: {dados['Atributos']['atl']:<4} EVA: {dados['Atributos']['eva']:<4} CAR: {dados['Atributos']['car']:<4}")

# Rolagem Leonine
@bot.command()
async def leonine(ctx):   
    
    channel = (ctx.channel)

    dados = player_leonine()

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention} \nNome: {dados["Nome"]:<10} Raça: {"Leonine":<10} PC: {dados["PC"]}\n'
      f"ARC: {dados['Atributos']['arc']:<4}  VIG: {dados['Atributos']['vig']:<4} DES: {dados['Atributos']['des']:<4} SAB: {dados['Atributos']['sab']:<4}\n"
      f"FOR: {dados['Atributos']['for']:<4} ATL: {dados['Atributos']['atl']:<4} EVA: {dados['Atributos']['eva']:<4} CAR: {dados['Atributos']['car']:<4}")

# Rolagem Felínio
@bot.command()
async def felinio(ctx):   
    
    channel = (ctx.channel)

    dados = player_felinio()

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention} \nNome: {dados["Nome"]:<10} Raça: {"Felínio":<10} PC: {dados["PC"]}\n'
      f"ARC: {dados['Atributos']['arc']:<4}  VIG: {dados['Atributos']['vig']:<4} DES: {dados['Atributos']['des']:<4} SAB: {dados['Atributos']['sab']:<4}\n"
      f"FOR: {dados['Atributos']['for']:<4} ATL: {dados['Atributos']['atl']:<4} EVA: {dados['Atributos']['eva']:<4} CAR: {dados['Atributos']['car']:<4}")

# Rolagem Chacálico
@bot.command()
async def chacalico(ctx):   
    
    channel = (ctx.channel)

    dados = player_chacalico()

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention} \nNome: {dados["Nome"]:<10} Raça: {"Chacalico":<10} PC: {dados["PC"]}\n'
      f"ARC: {dados['Atributos']['arc']:<4}  VIG: {dados['Atributos']['vig']:<4} DES: {dados['Atributos']['des']:<4} SAB: {dados['Atributos']['sab']:<4}\n"
      f"FOR: {dados['Atributos']['for']:<4} ATL: {dados['Atributos']['atl']:<4} EVA: {dados['Atributos']['eva']:<4} CAR: {dados['Atributos']['car']:<4}")

# Rolagem Javálion
@bot.command()
async def javalion(ctx):   
    
    channel = (ctx.channel)

    dados = player_javalion()

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention} \nNome: {dados["Nome"]:<10} Raça: {"Javalion":<10} PC: {dados["PC"]}\n'
      f"ARC: {dados['Atributos']['arc']:<4}  VIG: {dados['Atributos']['vig']:<4} DES: {dados['Atributos']['des']:<4} SAB: {dados['Atributos']['sab']:<4}\n"
      f"FOR: {dados['Atributos']['for']:<4} ATL: {dados['Atributos']['atl']:<4} EVA: {dados['Atributos']['eva']:<4} CAR: {dados['Atributos']['car']:<4}")

# Rolagem Reptilio
@bot.command()
async def reptilio(ctx):   
    
    channel = (ctx.channel)

    dados = player_reptilio()

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention} \nNome: {dados["Nome"]:<10} Raça: {"Reptilio":<10} PC: {dados["PC"]}\n'
      f"ARC: {dados['Atributos']['arc']:<4}  VIG: {dados['Atributos']['vig']:<4} DES: {dados['Atributos']['des']:<4} SAB: {dados['Atributos']['sab']:<4}\n"
      f"FOR: {dados['Atributos']['for']:<4} ATL: {dados['Atributos']['atl']:<4} EVA: {dados['Atributos']['eva']:<4} CAR: {dados['Atributos']['car']:<4}")

# Rolagem Ursárion
@bot.command()
async def ursarion(ctx):   
    
    channel = (ctx.channel)

    dados = player_ursa()

    await ctx.message.delete()    
        
    await channel.send(f'{ctx.author.mention} \nNome: {dados["Nome"]:<10} Raça: {"Denko":<10} PC: {dados["PC"]}\n'
      f"ARC: {dados['Atributos']['arc']:<4}  VIG: {dados['Atributos']['vig']:<4} DES: {dados['Atributos']['des']:<4} SAB: {dados['Atributos']['sab']:<4}\n"
      f"FOR: {dados['Atributos']['for']:<4} ATL: {dados['Atributos']['atl']:<4} EVA: {dados['Atributos']['eva']:<4} CAR: {dados['Atributos']['car']:<4}")

# Rolagem Tritão
@bot.command()
async def tritao(ctx):   
    
    channel = (ctx.channel)

    dados = player_tritao()

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention} \nNome: {dados["Nome"]:<10} Raça: {"Tritão":<10} PC: {dados["PC"]}\n'
      f"ARC: {dados['Atributos']['arc']:<4}  VIG: {dados['Atributos']['vig']:<4} DES: {dados['Atributos']['des']:<4} SAB: {dados['Atributos']['sab']:<4}\n"
      f"FOR: {dados['Atributos']['for']:<4} ATL: {dados['Atributos']['atl']:<4} EVA: {dados['Atributos']['eva']:<4} CAR: {dados['Atributos']['car']:<4}")

# Rolagem Denkomu
@bot.command()
async def denkomu(ctx):   
    
    channel = (ctx.channel)

    dados = player_denko()

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention} \nNome: {dados["Nome"]:<10} Raça: {"Denkomu":<10} PC: {dados["PC"]}\n'
      f"ARC: {dados['Atributos']['arc']:<4}  VIG: {dados['Atributos']['vig']:<4} DES: {dados['Atributos']['des']:<4} SAB: {dados['Atributos']['sab']:<4}\n"
      f"FOR: {dados['Atributos']['for']:<4} ATL: {dados['Atributos']['atl']:<4} EVA: {dados['Atributos']['eva']:<4} CAR: {dados['Atributos']['car']:<4}")

# Rolagem Aládico
@bot.command()
async def aladico(ctx):   
   
    channel = (ctx.channel)

    dados = player_aladico()

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention} \nNome: {dados["Nome"]:<10} Raça: {"Aladico":<10} PC: {dados["PC"]}\n'
      f"ARC: {dados['Atributos']['arc']:<4}  VIG: {dados['Atributos']['vig']:<4} DES: {dados['Atributos']['des']:<4} SAB: {dados['Atributos']['sab']:<4}\n"
      f"FOR: {dados['Atributos']['for']:<4} ATL: {dados['Atributos']['atl']:<4} EVA: {dados['Atributos']['eva']:<4} CAR: {dados['Atributos']['car']:<4}")

# Rolagem Nivólio
@bot.command()
async def nivolio(ctx):   
    
    channel = (ctx.channel)

    dados =player_nivolio()

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention} \nNome: {dados["Nome"]:<10} Raça: {"Nivolio":<10} PC: {dados["PC"]}\n'
      f"ARC: {dados['Atributos']['arc']:<4}  VIG: {dados['Atributos']['vig']:<4} DES: {dados['Atributos']['des']:<4} SAB: {dados['Atributos']['sab']:<4}\n"
      f"FOR: {dados['Atributos']['for']:<4} ATL: {dados['Atributos']['atl']:<4} EVA: {dados['Atributos']['eva']:<4} CAR: {dados['Atributos']['car']:<4}")

# Rolagem Humano
@bot.command()
async def humano(ctx):   
    
    channel = (ctx.channel)

    dados = player_humano()

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention} \nNome: {dados["Nome"]:<10} Raça: {"Humano":<10} PC: {dados["PC"]}\n'
      f"ARC: {dados['Atributos']['arc']:<4}  VIG: {dados['Atributos']['vig']:<4} DES: {dados['Atributos']['des']:<4} SAB: {dados['Atributos']['sab']:<4}\n"
      f"FOR: {dados['Atributos']['for']:<4} ATL: {dados['Atributos']['atl']:<4} EVA: {dados['Atributos']['eva']:<4} CAR: {dados['Atributos']['car']:<4}")

bot.run("MTEzMDE1OTEwMTIyMjA2MDExMg.GsovzO.oyFLnf0egvdhG8ySddCIaSFGZBFjIUJt3e3h2o")