from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Your bot's token from BotFather
TOKEN = "7571446967:AAEpkskfzsbmkfGxy0dwKaiYZwhjnD89mHo"

# /start command: Greets the user
def start(update, context):
    update.message.reply_text(
        "Hello! 👋 I'm your Telegram bot. Use /help to see what I can do!"
    )

# /help command: Provides a list of available commands
def help_command(update, context):
    update.message.reply_text(
        "Here are the commands you can use:\n"
        "/start - Start interacting with me\n"
        "/help - Show this help message\n"
        "/about - Learn more about me"
    )

# /about command: Introduces the bot
def about(update, context):
    update.message.reply_text(
        "I'm a simple Telegram bot created to help you with basic tasks. "
        "More features will be added soon!"
    )

# Handle text messages: Replies to any text message
def handle_message(update, context):
    user_message = update.message.text
    response = f"You said: {user_message}. That's interesting!"
    update.message.reply_text(response)

# Main function to run the bot
def main():
    # Create an updater and dispatcher
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("about", about))

    # Add message handler
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start polling and keep the bot running
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()