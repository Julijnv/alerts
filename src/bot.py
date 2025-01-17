from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from src.google_search import perform_google_search

# Cache to store previously fetched results
previous_results = set()

def start(update: Update, context: CallbackContext) -> None:
    """
    Handles the /start command and welcomes the user.

    Args:
        update (Update): The incoming Telegram update.
        context (CallbackContext): Context object containing bot and user data.
    """
    update.message.reply_text("Welcome! I will help you find new prete decks. Use /search to start.")

def search(update: Update, context: CallbackContext) -> None:
    """
    Executes the search command and sends new results to the user.

    Args:
        update (Update): The incoming Telegram update.
        context (CallbackContext): Context object containing bot and user data.
    """
    global previous_results
    update.message.reply_text("Searching for new results. Please wait...")
    
    results = perform_google_search()
    if results:
        new_results = set(results) - previous_results
        if new_results:
            for result in new_results:
                update.message.reply_text(f"New result found: {result}")
            previous_results.update(new_results)
        else:
            update.message.reply_text("No new results found at the moment.")
    else:
        update.message.reply_text("There was an issue retrieving results. Please try again later.")

def main():
    """
    Initializes the Telegram bot and starts listening for commands.
    """
    from config.settings import TELEGRAM_TOKEN

    # Initialize the updater and dispatcher
    updater = Updater(TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher

    # Register bot commands
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("search", search))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
