import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True


bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='createteams')
async def create_teams(ctx):
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    await ctx.send("How many teams?")
    try:
        num_teams = int((await bot.wait_for('message', check=check)).content)
    except ValueError:
        await ctx.send("Please enter a valid number.")
        return

    teams = {}
    for i in range(num_teams):
        await ctx.send(f"Name for team {i + 1}:")
        team_name = (await bot.wait_for('message', check=check)).content
        teams[team_name] = []

    await ctx.send("Enter player names separated by commas:")
    players = (await bot.wait_for('message', check=check)).content.split(',')

    random.shuffle(players)

    while players:
        for team in teams.keys():
            if players:
                teams[team].append(players.pop())
            else:
                break

    await ctx.send("Teams have been created:")
    for team, members in teams.items():
        await ctx.send(f"{team}: {', '.join(members)}")

bot.run('')
