import io
import json
from urllib import parse as urlparse

import discord
import requests

print("starting...")
try:
    with open("ConfigEnglishWADBOT.json", "r") as f:
        CONFIG = json.load(f)
except FileNotFoundError:
    with open("ConfigEnglishWADBOT.json", "w") as f:
        json.dump({'Wolfram_API_Token': 'YOURTOKEN', 'Discord_Bot_Token': 'YOURTOKEN',
                   'YourDiscordId': '0', 'Banlist': ["ip", "who am i"]}, f)
    raise Exception("Missing Config.json. I added it, please fill it out yourself! (Intended at first excecution)")
WABASICURL = str("http://api.wolframalpha.com/v1/simple?appid=" + str(CONFIG['Wolfram_API_Token']) + "&i=")
print("In order of your bot running correctly please ensure that your Tokens in Discordtoken.txt and Wolframtoken.txt "
      "are correct. Your Bot might crash or be unable to answer otherwise. \nPlease also check out "
      "https://github.com/The-Bow-Hunter/WolframAlphaDiscordBot !\n---WolframAlphaDiscordBot by The_Bow_Hunter---")


class MyClient(discord.Client):

    async def on_ready(self):
        # Bot is now online
        activity = discord.Game("w|a help")
        await self.change_presence(activity=activity)
        print("Up and running!")

    async def on_message(self, message):

        if message.author.bot:
            # Other Bots
            if client.user in message.mentions:
                await message.channel.send("You seem to be a bot, so this is a self destrutive message. "
                                           "I dont react to other bots, but you pinged me so you get this. "
                                           "Users please use w|a help", delete_after=20)
            return
        elif message.content.lower() == "w|a help":
            # This is the Bots helppage. Please leave the Information about me as the author and my Github Repository
            embed = discord.Embed(title="Wolfram|Alpha", url="https://wolframalpha.com",
                                  description="Bot to answer questions with Wolfram Alpha", color=0xff0a0a)
            embed.set_author(name="TM#5784", url="https://github.com/The-Bow-Hunter")
            embed.set_thumbnail(url="https://www.wolframalpha.com/_next/static/images/Logo_3KbuDCMc.svg")
            embed.add_field(name="Prefix", value="w|a", inline=False)
            embed.add_field(name="Usage", value="Simply write \"w|a \" (without \") and your question, "
                                                "just as you would in WA. It may need some time.", inline=False)
            embed.add_field(name="The Bot is slow",
                            value="That's normal. Wolfram Alpha needs its time to calculate and answer",
                            inline=False)
            embed.add_field(name="I want that bot on my Server",
                            value="checkout this Github Repository: "
                                  "https://github.com/The-Bow-Hunter/WolframAlphaDiscordBot/",
                            inline=False)
            embed.set_footer(
                text="Bot by TM#5784 This Bot is a public script and is in no association with "
                     "its author, Wolfram Alpha or Discord except that it uses its API")
            await message.channel.send(embed=embed)
            return
        elif message.content.lower().startswith("w|a "):
            # Main Function
            await message.add_reaction("✅")
            question = message.content
            question = question[4:]
            if question.lower() in CONFIG["Banlist"]:
                # banned questions (not all you should add, just as an example). In Order of protecting your ip
                print("A blocked question was asked by " + str(message.author))
                await message.channel.send("This question is blocked. Your trial was reported.")
                return
            questionurl = str(WABASICURL + str(urlparse.quote(question)))
            r = requests.get(questionurl)
            if r.content == "Error 1: Invalid appid":
                await message.channel.send("Wrong Appid")
            else:
                await message.channel.send(file=discord.File(fp=io.BytesIO(r.content), filename="WolframAlphaBot.gif"))
            return
        elif client.user in message.mentions:
            await message.channel.send("My Prefix is w|a. I help you with Math by sending Wolfram "
                                       "Alpha answers. To get more info write w|a help")
        # set your own id as id in order of adding a stop command only you can use
        elif message.author.id == CONFIG["YourDiscordId"] and message.content == "wabot stop":
            print("Shutting Bot down...")
            await self.close()


client = MyClient()
client.run(CONFIG["Discord_Bot_Token"])
