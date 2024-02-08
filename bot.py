import discord
from responses import Responses
from discord.ext import commands


def run_discord_bot():
    TOKEN = "MTIwNDk0ODk2NDYyMTgxMTcxMw.GQsAuQ.KbruT6v2Z8AlOlHMrhxdmi1se1yPsr6_cnj5HY"
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True

    bot = commands.Bot(command_prefix="/", intents=intents)

    @bot.event
    async def on_ready():
        await bot.add_cog(Responses(bot))
        print(f"{bot.user} is now running")
        print("Loaded cogs:", bot.cogs)

    @bot.event
    async def on_message(message):
        # want to differentiate between user and bot message
        if message.author == bot.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said '{user_message}' in '{channel}'")

        await bot.process_commands(message)

    bot.run(TOKEN)
