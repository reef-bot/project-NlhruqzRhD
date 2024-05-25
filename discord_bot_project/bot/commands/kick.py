# kick.py

import discord

from discord.ext import commands


class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick', help='Kick a member from the server')
    @commands.has_permissions(kick_members=True)
    async def kick_member(self, ctx, member: discord.Member, *, reason=None):
        try:
            await member.kick(reason=reason)
            await ctx.send(f'{member.mention} has been kicked from the server.')
        except discord.Forbidden:
            await ctx.send('I do not have permission to kick this member.')
        except discord.HTTPException:
            await ctx.send('An error occurred while trying to kick the member.')

def setup(bot):
    bot.add_cog(Kick(bot))