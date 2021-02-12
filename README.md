# WolframAlphaDiscordBot

## What is this?

This is an very simple script you can use in order of running a Discord Bot which is capable of taking a user send question and answering with an image of the answer by Wolfram Alpha

## Prerequisites

- Python 3.5.3 or higher
- discord.py (If it is your own computer "pip3 install discord.py" or "pip install discord.py" should work. If it isn't i assume you know a bit about python and your system. You can look in the [discord.py docs](https://discordpy.readthedocs.io/en/latest/intro.html#installing))

## Setting up the Bot
1. Clone this Repository to your system

2. Get yourself a Discord Bot token and paste it in [Discordtoken.txt](/Discordtoken.txt). You can alrady Invite your Bot to your server now (but it is just offline so far)
A tutorial how to create a discord Bot, get its Token and later invite it to your Server you can find at [the offical discord.py documentation](https://discordpy.readthedocs.io/en/latest/discord.html)

3. [Register for a Wolfram Alpha Api Acces.](https://products.wolframalpha.com/api/) Please notice that there is only a limited amount of calls per month for free. 
To get started, you must register a Wolfram ID and sign in to the Wolfram|Alpha Developer Portal. Upon logging in, go to the My Apps tab to start creating your first app.
Click the Sign up to get your first AppID button to start the app creation process. After a one-time survey about intended usage, the AppID creation dialog will appear. Give your application a name and a simple description to register an AppID. Take this Appid and put it into [Wolframtoken.txt](/Wolframtoken.txt)

4. Your bot is set up now. Simply run either German.py for the German version or English.py for the English version. If you are using Terminal please start the programm out of the directory it is in in order of it being capable of reading the Tokens

##FAQ

### Why don't I host it public
As mentioned earlier there are limited API calls for free. I want to safe mine for me and my friends. In Order of providing it to others i tried keeping the code as simple as possible (thats why i dont use the command extension) so everyone can read it in a minute to ensure it is safe. All I ask for you when using this code is to leave my name and this Github Repository on its helppage

### I want an other prefix
You can easily change the prefix in the code. Just replace all w|a with your custom prefix

### I have problems / it is not working
Please open an Issue here in Github

### I want to host it 24/7
Then you need to let your machine run 24/7 or you get yourself a VPS/Docker. Just search for it on the internet and follow there steps how to run a python script

### I dont trust you
You can simply read the code it is less than a 100 lines

### I dont want it as a gif
You can either add a converter or if you want it as messages you might wanna use the Full Api. This is a lot more complicated and scince my aim was to keep it under 100 lines it does simply not fit the project

### Can I host it and register it at a bot side?
No. Most botsites reject Copied Bots and if i should see a copy of my bot on a botpage i might report it myself
If you have that much API calls send me a message and we can talk about it
