import discord
from discord.ext import commands
import random
from infoes import infos, intro

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

opinions = ["Oh my god, such a nice information!",
            "That sounds so good!",
            "Thank you for sharing this with me!",
            "Woah! I'm glad to be informed about this!"]

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
    
@bot.command()
async def takeinfo(ctx):
    info, picture = infos()
    await ctx.send(info, file=picture)



@bot.command()
async def giveinfo(ctx):
    await ctx.send(random.choice(opinions))
    await ctx.send("Why don't you share this information with everyone? You can add your information to https://sakuura.pythonanywhere.com !")

bot.run("PUT YOUR TOKEN")
