import discord
from datetime import datetime
from discord.ext import commands
from discord import Color


class help(commands.Cog, name='help'):

  def __init__(self, bot):
      self.bot = bot
      self.bot.remove_command('help')

  @commands.command(name='help', brief="List every command of the bot")
  async def all_commands(self, ctx,*,args=""):
        """ Provide a list of every command available command for the user,
        split by extensions and organized in alphabetical order.
        Will not show the event-only extensions """
        embed = discord.Embed(title='Dungeon Master Help',description=f'Dungeon master is the best bot for your D&D SRD Needs. Embeds feature pages to keep data concise and easy to read.',color=Color.red())
        
        embed.add_field(name='`>races [args]`',value='Use this command to get info about D&D race, if args is included it will give info about that race otherwise it will list all races.',inline=False)
        embed.add_field(name='`>class [args] [levels]`',value='Use this command to get info about D&D class, if args is included it will give info about that class otherwise it will list all class. If `levels` is appended to the end it will give info about each level.',inline=False)
        embed.add_field(name='`>spells [args]`',value='Use this command to get info about D&D spell, if args is included it will give info about that spell otherwise it will list all races.',inline=False)
        embed.add_field(name='`>equipment [args]`',value='Use this command to get info about D&D equipment, if args is included it will give info about that equipment otherwise it will list all equipment. This includes armor, weapons, and other objects.',inline=False)
        
        embed.add_field(name='Links',value="[Bot Invite](https://discord.com/oauth2/authorize?client_id=755592938922442782&permissions=10304&scope=bot) , [Support Server](https://discord.com/invite/wV5YdX94h4)")
        
        embed.add_field(name="Number of guilds",value=len(self.bot.guilds))


        await ctx.send(embed=embed)
  
  @commands.command(
      name='ping',
        brief='returns bot latency'
        )
  async def ping(self,ctx):
    await ctx.send(f'Pong! {round(self.bot.latency *1000)}ms')
    

  @commands.Cog.listener()
  async def on_command_error(self,ctx, error):
        print(error)
        channel = self.bot.get_channel(790001914091274250)
        embed=discord.Embed(title='Command Error',description=f'`{ctx.message.content}` ran by {ctx.author.mention} in {ctx.channel.mention}',color=discord.Color.red(),timestamp=datetime.now())
        embed.add_field(name='Error',value=error)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await channel.send(embed=embed)
        if 'not found' not in str(error):
            await ctx.send(embed=embed)
            
  @commands.Cog.listener()
  async def on_command(self,ctx):
        print(f'command ran in {ctx.channel.name} by {ctx.author.name}')
        channel = self.bot.get_channel(790001914091274250)
        embed=discord.Embed(title='Command Logged',description=f'`{ctx.message.content}` ran by {ctx.author.mention} in {ctx.channel.mention}',color=0x008000,timestamp=datetime.now())
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await channel.send(embed=embed)


def setup(bot):
	bot.add_cog(help(bot))
