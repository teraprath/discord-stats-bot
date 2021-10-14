# Discord Stats Bot
A Simple Discord Bot with an User Stats System (Level, EXP and Ranks) using the [discord.py](https://discordpy.readthedocs.io/en/stable/) libary and a [MySQL-Databse](https://www.mysql.com/de/). It can be easily expanded with the [Discord Stats Web Panel](https://github.com/teraprath/discord-stats-web)
, which I also developed.

While this is easy to use, I recommend it as a base for a Discord Bot rather than a finished bot.

![Image](https://i.imgur.com/ZX2R5Fb.png)

## Installation

1. Download the source and upload it on your Linux Server.
2. Then install the **discord.py** libary:
```
python3 -m pip install -U discord.py
```
If you are using Windows, then the following should be used instead:
```
py -3 -m pip install -U discord.py
```
4. Set up your **MySQL database** and create a database.
5. Go to the uploaded folder in **config.py** and enter your MySQL data.
```python
# MySQL Database
host = "localhost" # Or your host
user = "root" # Or your username
password = "password" # Or your password
database = "dcstats" # Or your name

# Discord
token = ""
```
6. It is also important that you provide a bot token. If you don't know how to create a bot on Discord, [this video](https://www.youtube.com/watch?v=ibtXXoMxaho) might help you.
7. **Invite** your discord bot on your server
8. Paste the [Bot Token](https://www.writebots.com/discord-bot-token/) in **config.py** and save it
9. And now finally **start** the bot with the following commands (Linux):
```bash
cd /home/your-folder/
python3 bot.py
```
You can modify the bot as you want.

# Refine with Discord Stats Web

Download the [Discord Stats Web](https://github.com/teraprath/discord-stats-web) for free and have a good visualization of the statistics with a ranking system.

![Image](https://i.imgur.com/diEMgmM.png)
