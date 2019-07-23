import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
   print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
   channel = bot.get_channel(603086191553675293)
   await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
   channel = bot.get_channel(603086191553675293)
   await channel.send(f'{member} leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')

bot.run('NjAzMDYyMDg5NzI4MTMxMDcy.XTZ7hw.swNa_RQiA_w2__ffBhy3w4G9HyI')