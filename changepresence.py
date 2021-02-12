import discord

print("starting...")
f = open("Discordtoken.txt", "r")
DSTOKEN = str(f.read())
f.close()


class MyClient(discord.Client):

    async def on_ready(self):
        # activity = discord.CustomActivity("Prefix: w|a (w|a help for help)")
        activity = discord.Game("w|a help")
        await self.change_presence(activity=activity)
        print("Done!")


client = MyClient()
client.run(DSTOKEN)
