import datetime
import time
import platform
from Core.Utils.predicates import ReactionPredicate
from Core.Utils.menus import start_adding_reactions
import asyncio
import discord
from discord.ext import commands

from Core.config import logger
from Core.permissions import is_mod_or_superior


def setup(client):
    client.add_cog(Testing(client))


class Testing(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.role = None
        self.logged = False
        self.scuttle = 235148962103951360

    @commands.group(name="Testing", help="Commands not fully implemented yet.")
    async def Testing_Group(self):
        return cls.help

    @commands.command(name="test", usage=";ping")
    async def testreacts(self, ctx):
        msg = await ctx.send("Yay or Nay")
        start_adding_reactions(msg, ReactionPredicate.YES_OR_NO_EMOJIS)
        pred = ReactionPredicate.yes_or_no(msg, ctx.author)
        await ctx.bot.wait_for("reaction_add", check=pred)
        if pred.result is True:
            await ctx.send("You said YES")
        else:
            await ctx.send("You said NO")

    @commands.command()
    async def boop(self, ctx):
        await ctx.send("Edited Beep")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.lower().startswith("!executioner"):
            role_names = [role.name for role in message.author.roles]
            if any("Executioner" in x for x in role_names):
                await message.channel.send("Hey, You already have that!")
                return
            await asyncio.sleep(10)
            member = await message.guild.fetch_member(message.author.id)
            role_names = [role.name for role in member.roles]
            staff_channel = discord.utils.find(
                lambda c: c.id == 714277622716170280, self.client.get_all_channels()
            )
            if any("Executioner" in x for x in role_names):
                if self.logged == True:
                    await staff_channel.send(
                        "<@{0} appears to be working as functional again.".format(
                            self.scuttle
                        )
                    )
                self.logged = False
                return

            if not self.logged:
                await staff_channel.send(
                    "Heads up, <@{0}> took over 10 seconds to add Executioner to {1}. Adding now".format(
                        self.scuttle, message.author.mention
                    )
                )
                self.logged = True

            if self.role == None:
                new_strike = discord.utils.find(
                    lambda m: m.name == "Executioner", message.guild.roles
                )
            await message.author.add_roles(self.role)
            await message.delete()
            logger.GENERAL("Gave Executioner to {0}".format(str(message.author)))
