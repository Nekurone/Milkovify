from discord.ext import commands
from Core import permissions


class OwnerCog(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.last_cog = ""

    @commands.command()
    @commands.check(permissions.is_admin_or_superior)
    async def shutdown(self, ctx):
        await ctx.send("Shutting down, I love you.")
        await self.client.close()

    @commands.command()
    @commands.check(permissions.is_admin_or_superior)
    async def load(self, ctx, *, cog: str):
        """Command which loads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.client.load_extension("Cogs." + cog)
        except Exception as e:
            await ctx.send(f"**`ERROR:`** {type(e).__name__} - {e}")
        else:
            await ctx.send("**`SUCCESS`**\N{PISTOL}")

    @commands.command()
    @commands.check(permissions.is_admin_or_superior)
    async def unload(self, ctx, *, cog: str):
        """Command which Unloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.client.unload_extension("Cogs." + cog)
        except Exception as e:
            await ctx.send(f"**`ERROR:`** {type(e).__name__} - {e}")
        else:
            await ctx.send("**`SUCCESS`**\N{PISTOL}")

    @commands.command(name="reload")
    @commands.check(permissions.is_admin_or_superior)
    async def rel(self, ctx, *, cog: str):
        """Command which Reloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            if cog.lower() == "last":
                if self.last_cog != "":
                    cog = self.last_cog
                else:
                    await ctx.send(f"**`ERROR:`** No Last Cog")
            self.client.unload_extension("Cogs." + cog)
            self.client.load_extension("Cogs." + cog)
        except Exception as e:
            await ctx.send(f"**`ERROR:`** {type(e).__name__} - {e}")
        else:
            await ctx.send("**`SUCCESS`**\N{PISTOL}")
        self.last_cog = cog


def setup(client):
    client.add_cog(OwnerCog(client))
