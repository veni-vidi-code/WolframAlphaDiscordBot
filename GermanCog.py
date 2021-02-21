from io import BytesIO
from urllib import parse as urlparse

import requests
from discord import Embed, File
from discord.ext import commands


class WolframAlpha(commands.Cog, name="Server File Listener"):
    def __init__(self, bot: commands.Bot, token: str):
        """
        Wolfram Alpha Cog
        https://github.com/The-Bow-Hunter

        Nutzt die Wolfram Alpha Simple Api

        Denk daran einen gültigen Token anzugeben!
        """
        if token == "":
            raise Exception("Wolfram Alpha Token darf nicht leer sein! Bitte gib ihn mit in den Wolfram Alpha Cog")
        self.b = bot
        print("""
        *********************************
        Wolfram Alpha Cog hinzugefügt
        https://github.com/The-Bow-Hunter
        *********************************
        """)

        self.WABASICURL = str("http://api.wolframalpha.com/v1/simple?appid=" + token + "&i=")

    @commands.command(name="WolframAlpha",
                      help="Schreibe hinter den command deine Frage in Anführungszeichen (z.B. \"1+1\"), warte etwas "
                           "und erhalte die Antwort von "
                           "Wolfram Alpha. Schau doch mal auf [Github](https://github.com/The-Bow-Hunter)",
                      brief="Gibt dir ein Ergebnis von WolframAlpha", aliases=["wa", "w|a", "wolfram"])
    @commands.cooldown(2, 40, commands.BucketType.user)
    async def walpha(self, ctx: commands.context, arg):
        questionurl = str(self.WABASICURL + str(urlparse.quote(arg)))
        embed = Embed(title="Wolfram|Alpha", url="https://wolframalpha.com/",
                              description="Hier hast du deine Antwort von Wolfram Alpha")
        embed.set_author(name="WolframAlphaBot by TM", url="https://github.com/The-Bow-Hunter")
        embed.add_field(name="Github", value="https://github.com/The-Bow-Hunter", inline=False)
        embed.set_footer(text="Not supported by Wolfram Alpha in any way. This is a (possibly modified) copy of the "
                              "cog from https://github.com/The-Bow-Hunter")
        r = requests.get(questionurl)
        if r.content == "Error 1: Invalid appid":
            await ctx.reply("Es scheint als wäre ich momentan in Wartung. Sorry")
            print("Invalid appid error")
        else:
            await ctx.reply(file=File(fp=BytesIO(r.content), filename="WolframAlphaBot.gif"), embed=embed)
        return

    @walpha.error  
    async def walpha_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.reply(f"Du bist zu schnell! Versuche es erneut in {error.retry_after:.2f}s.",
                            delete_after=15)
