import datetime
import discord
import os
import random
from discord.ext import commands, tasks
from itertools import cycle

TOKEN = 'NzE5OTIzODM1MzczMjIzOTky.Xt-fUQ.lIHar3aw3IPrqr_HMPwFrLTvPHg'
Client = commands.Bot(command_prefix = "?")
Client.remove_command("help")
Status = cycle(["Minecraft for Smart Clocks", "Minecraft for Smart Fridge", "Minecraft for teddy bears", "Minecraft for spoon",
          "Minecraft for Youtube", "Minecraft for Twitch", "Minecraft for nukes", "Minecraft for Z2"])
def check_for_GodKiller(ctx):
    return ctx.author == 629243339379834880

@Client.event
async def on_ready():
    print('Logged in as')
    print(Client.user.name)
    print(Client.user.id)
    print('------')
    change_status.start()
    await Client.change_presence(status = discord.Status.dnd)

@Client.command()
async def help(ctx, command = "all"):
   if command == "all":
       await ctx.send(content = """
```
Present command are as follows:
1) ?help = Gives a list of all commands.
2) ?roast = Gives a roasting line.
3) ?ping = Gives the current ping of the bot.
4) ?clear = Deletes messages. (Note: If no integer value is provided then the bot will only delete your own message.)
5) ?kick = Kicks the member specified. (Note: If no member is mentioned the bot will raise an error.)
6) ?ban = Bans the member specified. (Note: If no member is mentioned the bot will raise an error.)
7) ?q = Asks a question.
8) ?weather = Tells the current weather (Note: Presently the bot can only tell Andheri's weather)
9) ?say = Tells the message specified.
10) ?spam = Will spam a message a specified number of times.
```""", delete_after = 600)

@Client.command()
async def cogs(ctx):
  await ctx.send(content = '''
  ```By default, most cogs are already loaded but if you still don't get the desired output you can type '?load <name of the cog>'. Below is the list of cogs:
  i)  Weather
  ii) Say```
  ''')

@Client.command()
async def kick(ctx, member : discord.member, *, reason = None):
    await member.kick(reason = reason)
    await ctx.send(f"Kicked {member}")

@kick.error
async def clear_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandInvokeError):
        await ctx.send("||_discord.ext.commands.errors.CommandInvokeError_.|| The bot raised an exception.")
    elif isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        await ctx.send("||_discord.ext.commands.errors.MissingRequiredArgument_.||The bot raised an exception. Please specify a valid member.")

@Client.command()
@commands.check(check_for_GodKiller)
async def unban(ctx, *, member):
    member_name, member_discriminator = member.split("#")
    banned_users = await ctx.guild.bans()
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {member_name}#{member_discriminator}")

@Client.command()
async def check(ctx):
    x = datetime.datetime.now()
    #day_name = x.strftime('%A')
    #day = x.strftime('%d')
    #month = x.strftime('%B')
    hour = x.strftime('%H')
    minute = x.strftime('%M')
    #await ctx.send(f'{day_name} {day}, {month} {hour}:{minute}')
    if hour == '16':
        if minute == '00':
            await ctx.send("@FIITJEE We have class.")
        else:
            await ctx.send("There is a class which is currently going on mf.")
    else:
        await ctx.send("No event found.")

@Client.command()
async def ban(ctx, member : discord.member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send(f'Banned {member}')

@Client.command()
async def q(ctx, *, question):
    responses = ["Yes", "Maybe", "No", "Absolutely", "Absolutely not", "I'm not sure"]
    if "gay" in question:
        if "you" in question:
            await ctx.send(content = "No", delete_after = 60)
        elif "Anirudh" in question:
            await ctx.send(content = "No", delete_after = 60)
        elif "GodKiller" in question:
            await ctx.send(content = "No", delete_after = 60)
        elif "godkiller" in question:
            await ctx.send(content = "No", delete_after = 60)
        elif "Godkiller" in question:
            await ctx.send(content = "No", delete_after = 60)
        elif "Android" in question:
            await ctx.send(content = "No", delete_after = 60)
        elif "anirudh" in question:
            await ctx.send(content = "No", delete_after = 60)
        elif "android" in question:
            await ctx.send(content = "No", delete_after = 60)
        elif "I" in question:
            await ctx.send(content = "No", delete_after = 60)
        elif "i" in question:
            await ctx.send(content = "No", delete_after = 60)
        elif "Prakhar" in question:
            await ctx.send(content = "Yes", delete_after = 60)
        else:
            await ctx.send(content = "Yes", delete_after = 60)
    else:
        await ctx.send(content = f'{random.choice(responses)}', delete_after = 60)

@Client.command()
async def ping(ctx):
    await ctx.send(f'Pong! That took around {round(Client.latency * 1000)} milliseconds.')

@Client.command()
async def clear(ctx, amount = 1):
    await ctx.channel.purge(limit = amount)

@tasks.loop(hours=2)
async def change_status():
    await Client.change_presence(activity=discord.Game(next(Status)))

@Client.command()
@commands.check(check_for_GodKiller)
async def load(ctx, extension):
    Client.load_extension(f'Cogs.{extension}')

@Client.command()
@commands.check(check_for_GodKiller)
async def unload(ctx, extension):
    Client.unload_extension(f'Cogs.{extension}')

@Client.command()
async def test(ctx):
    await ctx.send("<:Facepalm:706174157129515018>")

#for filename in os.listdir('./Cogs'):
 #   if filename.endswith(".py"):
  #      Client.load_extension(f'Cogs.{filename[:-3]}')

Client.run(TOKEN)
