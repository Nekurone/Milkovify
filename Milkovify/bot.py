from datetime import datetime

import discord
from discord.ext import commands

from Core.config import logger, PREFIX, DESCRIPTION, AUTHOR, VERSION

INTRO = "==========================\nMILKOVIFY - V:{0}\n==========================\n".format(
    VERSION
)


class Client(commands.Bot):
    def __init__(self, cogs):

        super().__init__(
            command_prefix=PREFIX, case_insensitive=True, description=DESCRIPTION
        )

        self.uptime = datetime.now()
        self._version = VERSION
        self.logger = logger
        self.logger.set_level("GENERAL")
        self.guild_constants = None

        for cog in cogs:
            try:
                self.load_extension("Cogs." + cog)
            except Exception as e:
                exc = "{}: {}".format(type(e).__name__, e)
                self.logger.CRITICAL("Cog Loading Failed: {0}\n{1}".format(cog, exc))
            else:
                self.logger.GENERAL("Cog Loading Successful: {0}".format(cog))
        self.logger.GENERAL(
            "{0} Out of {1} Cogs Loaded".format(len(self.cogs), len(cogs))
        )

        async def on_ready(self):
            guilds = len(self.guilds)
            users = len(set([m for m in self.get_all_members()]))
            INFO = [
                str(self.user),
                "Prefix: {0}".format(self.command_prefix),
                "Version: {0}".format(self.version),
                "Discord.py  Version: {0}".format(discord.__version__),
            ]
            if guilds:
                INFO.extend(("Servers: {}".format(guilds), "Users: {}".format(users)))
            else:
                print("Ready. I'm not in any server yet!")
            INFO.append(
                "{} cogs with {} commands".format(len(self.cogs), len(self.commands))
            )
            print(INFO)
