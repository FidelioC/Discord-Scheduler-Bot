import discord
import responses


# send message to current channel or private message
async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)

        if is_private:
            await message.author.send(response)  # send privately
        else:
            await message.channel.send(response)  # send to current channel
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = "MTIwNDk0ODk2NDYyMTgxMTcxMw.GQsAuQ.KbruT6v2Z8AlOlHMrhxdmi1se1yPsr6_cnj5HY"
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is now running")

    @client.event
    async def on_message(message):
        # want to differentiate between user and bot message
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said '{user_message}' in '{channel}'")

        if user_message[0] == "?":
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
