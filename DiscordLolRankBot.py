import discord
import requests
from bs4 import BeautifulSoup
from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    ''' Prints when the bot is online and ready '''
    print("Bot is ready")

@client.command()
async def info(self):
    ''' When called will return info on the bot '''
    output = discord.Embed(title='League Rank Bot', description='Gets LoL account rank from OP.GG', color=0x34a1eb)
    output.add_field(name='Author', value='TestieGoetze')
    output.add_field(name='Invite', value='https://discordapp.com/api/oauth2/authorize?client_id=654394113499725824&permissions=83968&scope=bot')
    await self.send(embed=output)

@client.command()
async def rank(self, *accts):
    ''' When called in discord will webscrape a players OP.GG rank and account link '''
    for acct in accts:
        aurl = ('https://na.op.gg/summoner/userName=' + acct)
        page = requests.get(aurl)
        try:
            an = BeautifulSoup(page.content, 'html.parser').find('span', attrs={'class': 'Name'})
            an = ''.join(list(BeautifulSoup.prettify(an)[21:-9]))
        except AttributeError as error:
            await self.send('The account' + '"' + acct + '"' + 'was not found')
        try:
            ar = BeautifulSoup(page.content, 'html.parser').find('div', attrs={'class': 'TierRank'})
            ar = ''.join(list(BeautifulSoup.prettify(ar)[24:-8]))
            alp = BeautifulSoup(page.content, 'html.parser').find('span', attrs={"class": "LeaguePoints"})
            alp = ''.join(list(BeautifulSoup.prettify(alp)[28:-9]))
            await self.send(aurl + '\n' + 'Summoner Name: ' + an + '\n' + 'Current Rank: ' + ar + '-' + alp)
        except AttributeError as error:
                await self.send(aurl + '\n' + 'Summoner Name: ' + an + '\n' + 'Current Rank: ' + (ar[9:]))
	    
client.run("NjU0Mzk0MTEzNDk5NzI1ODI0.XgO-fA.8s-3OH3K4HUZCsY479QcxoJ_uMQ")
