import os
from telethon import TelegramClient, events, Button
import json

# Read configurations from app.json file
with open('app.json') as f:
    app_config = json.load(f)

# Bot token obtained from BotFather
BOT_TOKEN = app_config.get('BOT_TOKEN')

# Owner's Telegram user ID
OWNER_ID = app_config.get('OWNER_ID')

# List of sudo users' Telegram user IDs
SUDO_USERS = app_config.get('SUDO_USERS')

# Heroku app name (optional)
HEROKU_APP_NAME = app_config.get('HEROKU_APP_NAME')

# Heroku API key (optional, required only if deploying to Heroku)
HEROKU_API_KEY = app_config.get('HEROKU_API_KEY')

