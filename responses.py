import random
import requests
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

    @commands.command()
    async def definition(self, ctx, word):
        base_url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        try:
            # request to WordsAPI
            response = requests.get(f"{base_url}")
            data = response.json()
            print(data)
            # Extract and concatenate all definitions into a string
            definitions_string = ""
            index = 1
            for meaning in data[0]["meanings"]:
                for definition_info in meaning["definitions"]:
                    definition = definition_info["definition"]
                    definitions_string += f"Definition {index}: {definition}\n\n"
                    index += 1

            # # Print the concatenated string
            # print(definitions_string)

            await ctx.send(definitions_string)

        except Exception as e:
            print(f"Failed to retrieve meaning: {e}")
            await ctx.send("Failed to retrieve the meaning. Please try again later.")

    @commands.command()
    async def create_event(self, ctx, date, time, location):
        init_reply = f"""new event received: 
        date: {date}
        time: {time}
        location: {location}"""

        await ctx.send(f"{init_reply}")


def setup(bot):
    bot.add_cog(Responses(bot))
