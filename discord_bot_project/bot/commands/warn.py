# warn.py

import discord

from discord.ext import commands

class Warn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='warn', help='Warn a user for inappropriate behavior')
    async def warn(self, ctx, member: discord.Member, *, reason=None):
        if ctx.message.author.guild_permissions.administrator:
            if member.guild_permissions.administrator:
                await ctx.send("You cannot warn an administrator.")
            else:
                # Logic for warning the user and logging the warning
                await ctx.send(f'{member.mention} has been warned for: {reason}')
                # Add logic for logging the warning
        else:
            await ctx.send("You do not have permission to warn users.")

def setup(bot):
    bot.add_cog(Warn(bot))