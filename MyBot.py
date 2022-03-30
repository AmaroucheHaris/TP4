from discord import Client
from argparse import ArgumentParser


class MyBot(Client):
    def __init__(self):
        super().__init__()
        self.run("OTU4Njg0MTU1NDIyNTkzMDU0.YkQ6Mg.2vXhRMfH-xONO6TyREPessiy_M8")

    async def on_ready(self):
        #self.log.infolog(f"{self.user} has connected to Discord!")
        print(f"{self.user} has connected to Discord")

    async def on_message(ctx, message):
        print(message.content)

        if message.content == "salut":
            await message.channel.send("Salut cousin")

        elif "reine des neiges" in message.content.lower():
            await message.channel.send("Libéré ! \nDélivré\nJe ne mentirai plus jamaaiiiiiiis !")
            message.content = ""

        elif "mp" in message.content.lower():
            await message.author.send("psssst, je me glisse dans tes mp")



bot = MyBot()

