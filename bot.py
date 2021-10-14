# Discord Stats Bot
# Author: https://github.com/teraprath

import discord
from discord import user
import database as db
import random
from config import token

db.init()

client = discord.Client(intents=discord.Intents.all())
prefix = "."

color_main = 0x7D7DFF
color_error = 0xFF3333

def get_needed_exp(level):
    return ((50*(level**2))+(50*level))

async def updateExp(user, channel, min_exp, max_exp, min_coins, max_coins):
    userid = user.id
    level = db.getUserData(userid, "level")
    exp = db.getUserData(userid, "exp")
    needed_exp = db.getUserData(userid, "nexp")

    exp += random.randint(min_exp, max_exp)
    db.updateUser(userid, "exp", exp)

    if exp >= needed_exp:
        db.updateUser(userid, "exp", 0)
        nexp = get_needed_exp(level+1)
        db.updateUser(userid, "nexp", nexp)
        db.updateUser(userid, "level", level+1)

        await client.get_channel(channel).send(f"💎 Congratulations {user.mention}, you are now **level {level+1}**.")
        db.updateRanking()

@client.event
async def on_ready():
    print(client.user.name + " connected to server.")
    db.updateRanking()

@client.event
async def on_member_join(member):
    if db.checkUser(member.id) == False:
        userid = member.id
        username = member.name
        discriminator = member.discriminator
        avatar = member.avatar_url
        db.registerUser(userid, username, discriminator, avatar)
        db.updateRanking()

@client.event
async def on_message(message):

    if message.author.bot:
        return

    if message.content.startswith(prefix):
        
        if message.content.startswith(prefix + "stats"):
            id = message.author.id
            level = db.getUserData(id, "level")
            exp = db.getUserData(id, "exp")
            needed_exp = db.getUserData(id, "nexp")
            embed = discord.Embed(title="", description=f"▸ Rank: 🏆 **#1**\n▸ Your Level: 💎 **{level}**\n▸ EXP: ☘️ **{exp}/{needed_exp}**", color=color_main)
            embed.set_author(name=f"{message.author.display_name}", icon_url=f"{message.author.avatar_url}")
            embed.set_thumbnail(url=f"{message.author.avatar_url}")
            embed.set_footer(text=f"{message.author}")
            await message.reply(embed=embed, mention_author=False)

        if message.content.startswith(prefix + "ranking"):
            list = db.getRanking()
            embed = discord.Embed(title="🏆 Ranking", description="Top 10 of All-Time", color=color_main)
            x = -1
            for user in list:
                x += 1
                userid = (list[x])[0]
                user = await client.fetch_user(userid)
                exp =  db.getUserData(userid, "exp")
                nexp =  db.getUserData(userid, "nexp")
                level =  db.getUserData(userid, "level")
                if x == 0:
                    embed.add_field(name=f"**{x+1}. {user}** 🥇", value=f"Level: 💎 **{level}** ▸ EXP: ☘️ **{exp}/{nexp}**", inline=False)
                elif x == 1:
                    embed.add_field(name=f"**{x+1}. {user}** 🥈", value=f"Level: 💎 **{level}** ▸ EXP: ☘️ **{exp}/{nexp}**", inline=False)
                elif x == 2:
                    embed.add_field(name=f"**{x+1}. {user}** 🥉", value=f"Level: 💎 **{level}** ▸ EXP: ☘️ **{exp}/{nexp}**", inline=False)
                else:
                    embed.add_field(name=f"**{x+1}. {user}**", value=f"Level: 💎 **{level}** ▸ EXP: ☘️ **{exp}/{nexp}**", inline=False)
            await message.reply(embed=embed, mention_author=False)

    else:
        await updateExp(message.author, message.channel.id, 4, 8, 1, 10)

client.run(token)