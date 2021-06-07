import discord


async def is_mod_or_superior(ctx):
    if (discord.utils.find(lambda r: r.name == "Moderator", ctx.message.guild.roles) in ctx.author.roles or
        discord.utils.find(lambda r: r.name == "Admin", ctx.message.guild.roles) in ctx.author.roles or
        ctx.author.id == 242398251855249428):
        return True
    return False

async def is_admin_or_superior(ctx):
    if  (discord.utils.find(lambda r: r.name == "Admin", ctx.message.guild.roles) in ctx.author.roles or
        ctx.author.id == 242398251855249428):
        return True
    return False


async def is_owner(ctx):
    if ctx.author.id == 242398251855249428:
        return True
    return False
