 import os
import logging
import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration
from telethon import TelegramClient, events

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize Sentry
sentry_logging = LoggingIntegration(
    level=logging.INFO,       # Capture info and above as breadcrumbs
    event_level=logging.ERROR  # Send errors as events
)

sentry_sdk.init(
    dsn=os.environ.get('SENTRY_DSN'),
    integrations=[sentry_logging]
)

# Load variables from environment variables (set in Heroku)
API_ID = int(os.environ.get('API_ID'))
API_HASH = os.environ.get('API_HASH')
BOT_TOKEN = os.environ.get('BOT_TOKEN')

# Create a TelegramClient instance
client = TelegramClient('vote_bot_session', API_ID, API_HASH)

# Handler for processing votes
@client.on(events.CallbackQuery(pattern=r'^vote_'))
async def vote_handler(event):
    await event.answer('Vote counted!')

# Handler for update button
@client.on(events.NewMessage(pattern='/update'))
async def update_handler(event):
    await event.respond('Here are the latest updates:\n1. Update 1\n2. Update 2')

# Handler for support button
@client.on(events.NewMessage(pattern='/support'))
async def support_handler(event):
    await event.respond('For support, join our Telegram group: [Support Group](https://t.me/BWANDARLOK)')

# Start the client
if __name__ == "__main__":
    try:
        client.start(bot_token=BOT_TOKEN)
        logging.info("Bot started successfully!")
        client.run_until_disconnected()
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        sentry_sdk.capture_exception(e)
