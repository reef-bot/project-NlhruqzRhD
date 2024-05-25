# bot.py

import discord
from discord.ext import commands

# Import all command files
from commands.kick import KickCommand
from commands.ban import BanCommand
from commands.mute import MuteCommand
from commands.warn import WarnCommand
from commands.message_logging import MessageLoggingCommand

# Import content scanner and moderator
from moderation.content_scanner import ContentScanner
from moderation.content_moderator import ContentModerator

# Import config file
from config.config import PREFIX

# Create bot instance
bot = commands.Bot(command_prefix=PREFIX)

# Initialize content scanner and moderator
content_scanner = ContentScanner()
content_moderator = ContentModerator()

# Command to kick a user
@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await KickCommand().execute(ctx, member, reason)

# Command to ban a user
@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await BanCommand().execute(ctx, member, reason)

# Command to mute a user
@bot.command()
async def mute(ctx, member: discord.Member, *, reason=None):
    await MuteCommand().execute(ctx, member, reason)

# Command to warn a user
@bot.command()
async def warn(ctx, member: discord.Member, *, reason=None):
    await WarnCommand().execute(ctx, member, reason)

# Command for message logging
@bot.event
async def on_message(message):
    await MessageLoggingCommand().execute(message)

# Content scanning and moderation
@bot.event
async def on_message(message):
    if content_scanner.scan(message.content):
        await content_moderator.moderate(message)

# Run the bot
bot.run("YOUR_DISCORD_TOKEN") # Remember to replace "YOUR_DISCORD_TOKEN" with your actual bot token