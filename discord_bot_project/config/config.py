# config.py

import os

# Bot configuration settings
BOT_PREFIX = "!"
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Database configuration settings
DB_HOST = "localhost"
DB_USER = "admin"
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = "discord_bot_db"

# API keys
NLTK_API_KEY = os.getenv("NLTK_API_KEY")
SCIKIT_LEARN_API_KEY = os.getenv("SCIKIT_LEARN_API_KEY")