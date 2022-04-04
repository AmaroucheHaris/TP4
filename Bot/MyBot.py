from discord import Client
from argparse import ArgumentParser
import logging

#import Log.Logger as Logger
#from Log.Logger import Logger
#from Log import Logger as Logger
#import Log.Logger

class MyBot(Client):
#class MyBot(commands.Bot)
    def __init__(self, token):
        super().__init__()
        #super().__init__(command_prefix="!haris")

        #logger = Logger()
        logging.basicConfig(filename='logs.log', level=logging.DEBUG, format='%(asctime)s %(message)s')
        #self.run("OTU4Njg0MTU1NDIyNTkzMDU0.YkQ6Mg.2vXhRMfH-xONO6TyREPessiy_M8")
        self.run(token)
        

    async def on_ready(self):
        #self.log.infolog(f"{self.user} has connected to Discord!")
        print(f"{self.user} has connected to Discord")
        #adrien = await self.fetch_user("687986326250848293")

       # while True:
           # await adrien.send("Libéré, délivré !!!!")

    #async def on_message(self,ctx, message):
    async def on_message(self, message):

        print(message.content)
        logging.info(message.content)
        #self.logger.log(message.content)

        if message.content == "salut":
            await message.channel.send("Salut cousin")

        elif "reine des neiges" in message.content.lower():
            await message.channel.send("Libéré ! \nDélivré\nJe ne mentirai plus jamaaiiiiiiis !")
            #message.content = ""

        elif "mp" in message.content.lower():
            await message.author.send("psssst, je me glisse dans tes mp")

        elif "citrouille" in message.content.lower():
            await message.channel.send(file=discord.File('/Users/harisamarouche/Documents/IUT-Montreuil/troll/citrouille.png'))



#bot = MyBot()

