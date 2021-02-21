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

        Using the Wolfram Alpha simple Api

        Remember to fill in a valid Token!
        """
        if token == "":
            raise Exception("Missing you Wolfram Alpha Token! Please fill it out in the WolframAlphaCog")
        self.b = bot
        print("""
        *********************************
        Wolfram Alpha Cog added
        https://github.com/The-Bow-Hunter
        *********************************
        """)

        self.WABASICURL = str("http://api.wolframalpha.com/v1/simple?appid=" + token + "&i=")

    @commands.command(name="WolframAlpha",
                      help="Write your command in \" (e.g. wa \"1+1\"), wait some time "
                           "and get your answer from "
                           "Wolfram Alpha. Also check out this bot on Github [Github](https://github.com/The-Bow-Hunter)",
                      brief="Returns a wolfram Alpha answer", aliases=["wa", "w|a", "wolfram"])
    @commands.cooldown(2, 40, commands.BucketType.user)
    async def walpha(self, ctx: commands.context, arg):
        questionurl = str(self.WABASICURL + str(urlparse.quote(arg)))
        embed = Embed(title="Wolfram|Alpha", url="https://wolframalpha.com/",
                              description="Your answer by Wolfram Alpha")
        embed.set_author(name="WolframAlphaBot by TM", url="https://github.com/The-Bow-Hunter")
        embed.add_field(name="Github", value="https://github.com/The-Bow-Hunter", inline=False)
        embed.set_footer(text="Not supported by Wolfram Alpha in any way. This is a (possibly modified) copy of the "
                              "cog from https://github.com/The-Bow-Hunter")
        r = requests.get(questionurl)
        if r.content == "Error 1: Invalid appid":
            await ctx.reply("It seems as i have a wrong Appid. Sorry")
            print("Invalid appid error")
        else:
            await ctx.reply(file=File(fp=BytesIO(r.content), filename="WolframAlphaBot.gif"), embed=embed)
        return

    @walpha.error  # We do want to let people know why they do not get an answer
    async def walpha_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.reply(f"You are sending this command to fast! Try again in {error.retry_after:.2f}s.",
                            delete_after=15)
