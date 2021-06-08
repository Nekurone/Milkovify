from bot import Client
from Core.config import logger, TOKEN

"""
Runs the client. When adding new Cogs. Be sure to add them to COGS in here so the bot can load them.

todo: Rewrite
"""
COGS = ["owner", "stats", "testing", "markov"]


def main():
    client = Client(COGS)
    logger.GENERAL("Booting Bluebell Core with {0} Cogs.".format(len(COGS)))
    client.run(TOKEN)


main()
