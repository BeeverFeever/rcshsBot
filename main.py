#IMPORTS
import nextcord
import botPrefixes as bp
from nextcord.ext import commands

#NOT TO BE EDITED!
with open("token.txt") as f:
    TOKEN = f.readline()

def get_prefix(bot, message):
    return commands.when_mentioned_or(*bp.prefixes)(bot, message)

# If you make your own cog file, add it in a similar way that basic is added here, with 'cogs.<filename>'
extensions = ["cogs.basic","cogs.music", "cogs.moderation.prefix_control"]


bot = commands.Bot(
    command_prefix=get_prefix, description="Bot for the r/CSHighschoolers discord server")

if __name__ == "__main__":
    for extension in extensions:
        print(f"Loading {extension}...")
        bot.load_extension(extension)
print("Loaded extensions")


@bot.event
async def on_ready():
    print(
        f"\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {nextcord.__version__}\n"
    )


# This will handle events but if you dont handle every single error you can get, some might slip by without you knowing.
# For more info watch (https://youtu.be/_2ifplRzQtM?list=PLW3GfRiBCHOhfVoiDZpSz8SM_HybXRPzZ)
# 
# @bot.event
# async def on_command_error(ctx, error):
#     if isinstance(error, commands.MissingRequiredArgument):
#         await ctx.reply("Please pass in all required arguments.")

bot.run(TOKEN, reconnect=True) #  bot=True,
