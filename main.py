import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import random
from infoes import infos, intro
#from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

opinions = ["""Oh my god, such a nice information!",
            "That sounds so good!",
            "Thank you for sharing this with me!",
            "Woah! I'm glad to be informed about this!"""
            
            "Ne kadar da güzel bir bilgi!",
            "Kulağa ilgi çekici geliyor!",
            "Bunu benimle paylaştığın için teşekkür ederim!",
            "Vay canına! Bununla ilgili bilgi aldığıma memnun oldum!"]

wrrors = ["""Uh oh, something went wrong...",
          "Uh oh, something went wrong!",
          "Seems like the bot is unable to respond to this command for now.",
          "This command is not available at the moment, coming soon!"""
          
          "Tüh, bir şeyler yanlış gitti...",
          "Bir şeyler yanlış gitti! Hata 404!",
          "Bot şimdilik bu komuta cevap veremiyor gibi görünüyor."
          "Bu komut şu anlık müsait değil!"]

# error_message = "There is no command like that!"
error_message = "Böyle bir komut yok!"

@bot.event
async def on_ready():
        print(f'Logged in as {bot.user.name} ({bot.user.id})')
        print('------')

        # Iterate through all guilds the bot is a member of
        for guild in bot.guilds:
            print(f'Connected to guild: {guild.name} ({guild.id})')
            # Get the default channel for the guild
            default_channel = guild.text_channels[0]
            # Send a welcome message
            introduction, picture = intro()
            await default_channel.send(introduction, file=picture)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send(error_message)
    raise error

@bot.command()
async def takeinfo(ctx):
    info, picture = infos()
    await ctx.send(info, file=picture)



@bot.command()
async def giveinfo(ctx):
    await ctx.send(random.choice(opinions))
    # await ctx.send("Why don't you share this information with everyone? You can add your information to https://sakuura.pythonanywhere.com !")
    await ctx.send("Neden bu bilgiyi herkesle paylaşmıyorsun? Verdiğin bilgiyi https://sakuura.pythonanywhere.com genel ağ sitesine ekleyebilirsin!")

@bot.command()
async def predictype(ctx):
     await ctx.send(random.choice(wrrors))


bot.run("YOUR TOKEN HERE")
