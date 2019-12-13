import discord
import requests
from bs4 import BeautifulSoup
from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def info(pra):
    output = discord.Embed(title="League Rank Bot", description="Gets LoL account rank from OP.GG", color=0x34a1eb)
    output.add_field(name="Author", value="TestieGoetze")
    output.add_field(name="Invite", value="[Invite link]")
    await pra.send(embed=output)

@client.command()
async def rank(pra, acct):
    AcctURL = ('https://na.op.gg/summoner/userName=' + acct)
    page = requests.get(AcctURL)

    AcctLvL = BeautifulSoup(page.content, 'html.parser').find('span', attrs= {"title": "Level"})
    AcctLvL = ''.join(list(BeautifulSoup.prettify(AcctLvL)[40:-9]))
    print(AcctLvL)
    AcctLP = BeautifulSoup(page.content, 'html.parser').find('span', attrs={"class": "LeaguePoints"})
    AcctLP = ''.join(list(BeautifulSoup.prettify(AcctLP)[28:-9]))
    AcctName = BeautifulSoup(page.content, 'html.parser').find('span', attrs={"class": "Name"})
    AcctName = ''.join(list(BeautifulSoup.prettify(AcctName)[21:-9]))
    AcctRank = BeautifulSoup(page.content, 'html.parser').find('div', attrs={"class": "TierRank"})
    AcctRank = ''.join(list(BeautifulSoup.prettify(AcctRank)[24:-8]))
    if int(AcctLvL) < 30:
        await pra.send(AcctURL + '\n' + 'Summoner Name: ' + AcctName + '\n' + 'Current Rank: UNRANKED')
    await pra.send(AcctURL + '\n' + 'Summoner Name: ' + AcctName + '\n' + 'Current Rank: ' + AcctRank + '-' + AcctLP)

client.run("NjU0Mzk0MTEzNDk5NzI1ODI0.XfFmYQ.b6ioEx_Um0dyX28SiIManO9U7Yo")
#<span class="Level tip tpd-delegation-uid-1" title>146</span>