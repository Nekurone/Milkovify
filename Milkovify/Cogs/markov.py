import json
import discord
from discord.ext import commands
import markovify


def setup(client):
    client.add_cog(MarkovCog(client))


class MarkovCog(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.model = None

    def save_markov(self):
        model_json = self.model.to_json()
        try:
            with open('markov_data.json', 'w') as f:
                json.dump(model_json, f)
                print("Saved json")
                return 0
        except Exception as e:
            print("Error saving: {0}".format(e))
            return e

    def train_markov(self):
        with open('milkmessages.txt', 'r') as f:
            text = f.read()
        self.model = markovify.Text(text,
                                    state_size=4,
                                    well_formed=True
                                    )

    def get_markov_text(self):
        return self.model.make_sentence()

    @commands.Cog.listener()
    async def on_message(self, message):
        if str(message.user.id) != '277272009824665600':
            return
        if 0 != len(message.raw_mentions) + \
                len(message.raw_channel_mentions) + \
                len(message.raw_role_mentions) + \
                len(message.attachments):
            return

        cleaned_message = discord.utils.escape_markdown(message.clean_content())
        if cleaned_message[-1] != ".":
            cleaned_message += "."
        with open('milkmessages.txt','w') as f:
            f.write('\n{0}'.format(cleaned_message))
            f.close()

    @commands.command(name='train')
    async def train(self, ctx):
        print("Now training Milk's Markov Model. Please wait.")
        self.train_markov()
        print('Trained.')
        await ctx.send("Markov Model retrained. Give me a go <3")

    @commands.command()
    async def markov(self,ctx):
        t = self.get_markov_text()
        await ctx.send(t)


