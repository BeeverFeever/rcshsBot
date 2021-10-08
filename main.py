#IMPORTS
import nextcord
from nextcord.ext import commands

#NOT TO BE EDITED!
with open('token.txt') as f:
    TOKEN = f.readline()

def get_prefix(bot, message):
    # The prefix for bot commands
    prefixes = ["."]

    return commands.when_mentioned_or(*prefixes)(bot, message)

# If you make your own cog file, add it in a similar way that basic is added here, with 'cogs.<filename>'
extensions = ['cogs.basic','cogs.music']

bot = commands.Bot(
    command_prefix=get_prefix, description='Bot for the r/CSHighschoolers discord server')

if __name__ == '__main__':
    for extension in extensions:
        print(f"Loading {extension}...")
        bot.load_extension(extension)
print("Loaded extensions")


@bot.event
async def on_ready():
    print(f'\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {nextcord.__version__}\n')

@bot.event
async def on_ready():
    for guild in bot.guilds:
        for channel in guild.text_channels :
            if str(channel) == "🌎-general" or str(channel) == "𝕋𝕒𝕝𝕜𝕤" :
                Embed = nextcord.Embed()
                Embed.set_image(url="https://c.tenor.com/Fi1DbctJXQQAAAAC/what-what-up.gif")
                await channel.send(embed=Embed)
        print('Active in {}\n Member Count : {}'.format(guild.name,guild.member_count))

bot.run(TOKEN, reconnect=True)