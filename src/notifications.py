from telegram import Bot
from config.settings import TELEGRAM_TOKEN

def send_notification(chat_id, message):
    """
    Sends a notification to a specific Telegram chat.

    Args:
        chat_id (str): The unique identifier for the Telegram chat.
        message (str): The message content to be sent.
    """
    try:
        bot = Bot(token=TELEGRAM_TOKEN)
        bot.send_message(chat_id=chat_id, text=message)
    except Exception as e:
        print(f"Error sending Telegram notification: {e}")
