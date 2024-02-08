import random


def handle_response(message) -> str:
    # can always process any message in lower case
    p_message = message.lower()

    if p_message == "hello":
        return "Hallow"

    if p_message == "roll":
        return str(random.randint(1, 6))

    if p_message == "!help":
        return "`Helep helep!`"
