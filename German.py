import io
import json
from urllib import parse as urlparse

import discord
import requests

print("starting...")
try:
    with open("ConfigGermanWADBOT.json", "r") as f:
        CONFIG = json.load(f)
except FileNotFoundError:
    with open("ConfigGermanWADBOT.json", "w") as f:
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
            if client.user in message.mentions:
                await message.channel.send("Du scheinst ein Bot zu sein, deshalb wird meine Nachricht sofort wierder "
                                           "gelöscht werden. Ich reagiere nicht auf andere Bots. "
                                           "(außer sie erwähnen mich wie du) Wenn ein Nutzer das lesen sollte "
                                           "kann er mich "
                                           "mit w|a help ansprechen", delete_after=20)
            return
        elif message.content.lower() == "w|a help":
            # This is the Bots helppage. Please leave the Information about me as the author and my Github Repository
            embed = discord.Embed(title="Wolfram|Alpha", url="https://wolframalpha.com",
                                  description="Bot der Wolfram Alpha Seiten direkt in Discord sendet", color=0xff0a0a)
            embed.set_author(name="TM#5784", url="https://github.com/The-Bow-Hunter")
            embed.set_thumbnail(url="https://www.wolframalpha.com/_next/static/images/Logo_3KbuDCMc.svg")
            embed.add_field(name="Prefix", value="w|a", inline=False)
            embed.add_field(name="Nutzung", value="Schreibe einfach \"w|a \" (ohne Anführungszeichen) und dann den "
                                                  "Befehl den du auch in Wolfram Alpha eingeben würdest", inline=False)
            embed.add_field(name="Der Bot lädt lange",
                            value="Das ist normal. Wolfram Alpha braucht einen Moment um deine Ergebnisse zu berechnen "
                                  "genauso wie auf der Seite selbst",
                            inline=False)
            embed.add_field(name="Ich will den Bot auf meinem Server haben",
                            value="checkout this Github Repository: "
                                  "https://github.com/The-Bow-Hunter/WolframAlphaDiscordBot/",
                            inline=False)
            embed.set_footer(
                text="Bot by TM#5784 Dieser Bot wird in keiner Weise von Wolfram Alpha oder Discord unterstützt und "
                     "basiert nur auf der offiziellen Api")
            await message.channel.send(embed=embed)
            return
        elif message.content.lower().startswith("w|a "):
            await message.add_reaction("✅")
            question = message.content
            question = question[4:]
            if question.lower() in CONFIG["Banlist"]:
                """nichtgewollte Anfragen. Diese erscheinen nur in der Console und werden nicht geloggt, wer das für 
                sinvoll hält kann es gerne ergänzen"""
                print("Eine Anfrage aus der Sperrliste wurde von " + str(message.author) + " versucht.")
                await message.channel.send("Diese Frage ist gesperrt. Vermutlich um die IP des Bots geheim zu halten. "
                                           "Deine Anfrage wird in der Console erscheinen")
                return
            questionurl = str(WABASICURL + str(urlparse.quote(question)))
            embed = discord.Embed(title="Wolfram|Alpha", url="https://wolframalpha.com/",
                                  description="Hier hast du deine Antwort von Wolfram Alpha")
            embed.set_author(name="TM")
            embed.set_footer(text="Bot by Tom")
            r = requests.get(questionurl)
            if r.content == "Error 1: Invalid appid":
                await message.channel.send("Wrong Appid")
            else:
                await message.channel.send(embed=embed)
                await message.channel.send(file=discord.File(fp=io.BytesIO(r.content), filename="WolframAlphaBot.gif"))
            return
        elif client.user in message.mentions:
            await message.channel.send("Mein Prefix ist w|a. Ich helfe bei Mathe indem ich Wolfram "
                                       "Alpha Antworten sende. Wenn du mehr wissen willst schreibe bitte w|a help")
        elif message.author.id == int(CONFIG["YourDiscordId"]) and message.content == "wabot stop":
            print("Shutting Bot down...")
            await self.close()


client = MyClient()
client.run(str(CONFIG["Discord_Bot_Token"]))
