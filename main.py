import discord
from discord.ext import commands
from Config import CFG
import asyncio
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=CFG['Prefix'], intents=intents)

bot.remove_command('help')


@bot.event
async def on_ready():
    print('bot connected')


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(986654062760058920)
    role = discord.utils.get(member.guild.roles, id=986708938307276870)
    await member.add_roles(role)
    await channel.send(f'Member joined: [ID: {member.id}, Mention: {member.mention}, Name: {member.name}]')

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(986654062760058920)
    role = discord.utils.get(member.guild.roles, id=986708938307276870)
    await member.add_roles(role)
    await channel.send(f'Member joined: [ID: {member.id}, Mention: {member.mention}, Name: {member.name}]')


@bot.event
async def on_member_leave(member):
    channel = bot.get_channel(986654062760058920)
    await channel.send(f'Member leave: [ID: {member.id}, Mention: {member.mention}, Name: {member.name}]')


@bot.command()
async def verify(ctx):
    author = ctx.message.author
    guild = bot.get_guild(986650706347950153)
    notverifyrole = guild.get_role(986708938307276870)
    verifyrole = guild.get_role(986710307525259264)
    await author.remove_roles(notverifyrole)
    await author.add_roles(verifyrole)
    await ctx.channel.purge(limit=1)


@bot.command()
async def send(member: discord.Member, *, message):
    await member.send(message)


@bot.command()
@commands.has_permissions(ban_members=True)
async def tempban(ctx, member: discord.User, time: int, *, reason):
    channel = bot.get_channel(986654062760058920)
    await ctx.guild.ban(member, reason=reason)
    await channel.send(f"This member: {member.id} | {member.mention} has been banned by {ctx.author.mention} | {ctx.author.id}")
    await asyncio.sleep(time)
    await ctx.guild.unban(member)
    await channel.send(f"This member: {member.id} | {member.mention} has been unbanned! Yay.")


@bot.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, limit: int):
    await ctx.channel.purge(limit=limit)


@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Help", colour=discord.Colour.from_rgb(255, 125, 0))
    embed.add_field(name='help', value='View list commands', inline=False)
    embed.add_field(name='purge', value='Cleaning  (can only members who have permission: manage_messages)', inline=False)
    embed.add_field(name='tempban', value='Temp ban / Temporary ban (can only members who have permission: ban_members)', inline=False)

    await ctx.send(embed=embed)

bot.run(CFG['Bottoken'])
