import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import time

load_dotenv()

TOKEN = os.environ["TOKEN"]


intents = discord.Intents.default()
intents.message_content = True
intents.members = True


bot = commands.Bot(intents=intents, command_prefix="!")


@bot.event
async def on_ready():
    print('Were good to go')
    
@bot.event
async def on_message(message):
    if not message.guild:
        await bot.process_commands(message)
        return print(f" Dm to Bot: {message.content} ::::::: {message.author}")
    if message.guild:
        await bot.process_commands(message)
        return print(message.content)
    

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)
    
@bot.command()
async def members(ctx):
    for guild in bot.guilds:
        for member in guild.members:         
            await ctx.author.send(member)   

@bot.command()
async def DM(ctx, user: discord.User = None, *, value = None):
    if user == ctx.message.author:
        await ctx.send("Cannot message yourself, please try another User")
    else:
        await ctx.message.delete()
        if user == None:
            await ctx.send(f'{ctx.message.author}, Enter someone to DM.')
        else:
            if value == None:
                await ctx.send(f'{ctx.message.author}, Please enter a message to send with the DM.')
            else:
                await user.send(value)
                
                
@bot.command()
async def playing(ctx, *, message=None):
    if message == None:
        await ctx.send(f'{ctx.message.author}, Please mention a game ex. !playing Minecraft.')
                     
    else:    
        guild = ctx.guild
        for member in guild.members:
            if member == ctx.message.author:
                pass
            try:
                if member != None:
                    time.sleep(1)
                    messages = f' {ctx.message.author} is about to play {message}, Come Join {member} (LAST TEST IM SORRY) '
                    await member.send(messages)
                    await print("sent message")
            except:
                print("Error")
        

bot.run(TOKEN)
