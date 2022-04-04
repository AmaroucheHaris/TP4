import logging

class Logger:
    
    def __init__(self):
        logging.basicConfig(filename='logs.log', level=logging.DEBUG, format='%(asctime)s %(message)s')

    def log(message):
        logging.info(message.content)

