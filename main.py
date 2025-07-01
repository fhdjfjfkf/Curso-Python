import discord
from discord.ext import commands
from secret import TOKEN
import random

description = '''Hola como estas?'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='%', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def coinflip(ctx, coinflipamount=None):
    """Tira una moneda"""
    try:
        if coinflipamount is None:
            coinflipamount = 1
        else:
            coinflipamount = int(coinflipamount)

        
        if coinflipamount < 1 or coinflipamount > 50:
            await ctx.send("Solo puedes lanzar entre 1 y 50 monedas")
            return

        
        resultado = [random.choice(['Cara', 'Cruz']) for _ in range(coinflipamount)]
        await ctx.send('\n'.join(resultado))

    except ValueError:
        await ctx.send("El valor ingresado no es un número válido.")



bot.run(TOKEN)
