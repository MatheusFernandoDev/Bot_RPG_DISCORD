
import random


from defs.vampirico import merc_vamp, player_vamp
from defs.arqueonte import merc_arque, player_arque
from defs.elfo import merc_elfo, player_elfo
from defs.simio import merc_simio, player_simio
from defs.orc import merc_orc, player_orc
from defs.magmamir import merc_magma, player_magma
from defs.anao import merc_anao, player_anao
from defs.voidling  import merc_void, player_void
from defs.troll import merc_troll, player_troll
from defs.lupinico import merc_lupin, player_lupin
from defs.taurus import merc_tauru, player_tauru
from defs.lonine import merc_leonine, player_leonine
from defs.felinio import merc_felinio, player_felinio
from defs.chacalico import merc_chacalico, player_chacalico
from defs.javalion  import merc_javalion, player_javalion
from defs.reptilio import merc_reptilio, player_reptilio
from defs.ursarion import merc_ursa, player_ursa
from defs.tritao import merc_tritao, player_tritao
from defs.denkomu import merc_denko, player_denko
from defs.aladico import merc_aladico, player_aladico
from defs.nivolio import merc_nivolio, player_nivolio
from defs.humano import merc_humano, player_humano
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
  
    racas_funcoes = {
    "Vampirico": merc_vamp,
    "Arqueonte": merc_arque,
    "Elfo": merc_elfo,
    "Símio": merc_simio,
    "Orc": merc_orc,
    "Magmamir": merc_magma,
    "Anão": merc_anao,
    "Voidling": merc_void,
    "Troll": merc_troll,
    "Lupínico": merc_lupin,
    "Taurus": merc_tauru,
    "Leonine": merc_leonine,
    "Felínio": merc_felinio,
    "Chacálico": merc_chacalico,
    "Javálion": merc_javalion,
    "Reptilio": merc_reptilio,
    "Ursárion": merc_ursa,
    "Denkomu": merc_denko,
    "Aládico": merc_aladico,
    "Nivólio": merc_nivolio,
    "Humano": merc_humano
}
    
    # Escolha aleatória de uma raça
    raca_escolhida = random.choice(list(racas_funcoes.keys()))

    # Chama a função correspondente à raça escolhida
    dados = racas_funcoes[raca_escolhida]()

    channel = (ctx.channel)
    
    await ctx.message.delete()
    print(dados)

    await channel.send(f'{ctx.author.mention} \nNome: {dados["Nome"]:<10} Raça: {raca_escolhida:<10} PC: {dados["PC"]}  Classe:  {dados["Classe"]}\n'
      f"ARC: {dados['Atributos']['arc']:<4}  VIG: {dados['Atributos']['vig']:<4} DES: {dados['Atributos']['des']:<4} SAB: {dados['Atributos']['sab']:<4}\n"
      f"FOR: {dados['Atributos']['for']:<4} ATL: {dados['Atributos']['atl']:<4} EVA: {dados['Atributos']['eva']:<4} CAR: {dados['Atributos']['car']:<4}\n"
      f"\nProteção: \n{escolha_armaduras():<4}")
      #f"Nome: {dados['Equipamento']['nome']} Dano: {dados['Equipamento']['dano']} {dados['Equipamento']['tipo']} {dados['Equipamento']['peso']}")
    
       
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

bot.run("MTEzMDE1OTEwMTIyMjA2MDExMg.GzPFy6.YA9gC3-cJNxQVzGkvguZ5OGXSIHERaBgJqyBps")