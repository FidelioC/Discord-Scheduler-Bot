import random
from discord.ext import commands


class Responses(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("hello!")

    @commands.command()
    async def roll(self, ctx):
        await ctx.send(str(random.randint(1, 6)))


def setup(bot):
    bot.add_cog(Responses(bot))
