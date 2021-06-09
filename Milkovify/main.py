from bot import Client
from Core.config import logger, TOKEN

"""
Runs the client. When adding new Cogs. Be sure to add them to COGS in here so the bot can load them.

todo: Rewrite
"""
COGS = ["owner", "stats", "markov"]


def main():
    client = Client(COGS)
    logger.GENERAL("Booting Bluebell Core with {0} Cogs.".format(len(COGS)))
    client.run(TOKEN)

    @client.event()
    async def on_ready(self):
        guilds = len(client.guilds)
        users = len(set([m for m in client.get_all_members()]))
        INFO = [
            str(client.user),
            "Prefix: {0}".format(client.command_prefix),
            "Version: {0}".format(client.version),
            "Discord.py  Version: {0}".format(discord.__version__),
        ]
        if guilds:
            INFO.extend(("Servers: {}".format(guilds), "Users: {}".format(users)))
        else:
            print("Ready. I'm not in any server yet!")
        INFO.append(
            "{} cogs with {} commands".format(len(client.cogs), len(client.commands))
        )
        print(INFO)



main()
