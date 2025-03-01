from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Replace 'YOUR_TOKEN' with the token you got from BotFather
TOKEN = '7269368738:AAHvj7wLpOtEKj2RK6xrwgv_JM3PAdH86lw'

# Define the options and their corresponding links
OPTIONS_LINKS = {
    "Wondershare Filmora 14": "https://link-target.net/1308362/wondershare-filmora-14",
    "Wise Memory Optimizer": "https://link-center.net/1308362/wisememoryoptimizer",
    "Ms Office 2024": "https://link-target.net/1308362/microsoft-office-2024",
}

# Command to start the bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Welcome message with donation information
    welcome_message = (
        "Hi, welcome to BPS Tech Solution Bot!\n\n"
        "My developer is just a 2nd-year college student pursuing a course in Information Technology. "
        "You can support him by donating to his PayPal or GCash account below:\n\n"
        "**PayPal**: [Your PayPal Link or Email]\n"
        "**GCash**: [Your GCash Number]\n\n"
        "Thank you for your support! 😊"
    )

    # Create the inline keyboard with options
    keyboard = [
        [InlineKeyboardButton(option, callback_data=option)] for option in OPTIONS_LINKS.keys()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send the welcome message and the options
    await update.message.reply_text(welcome_message, reply_markup=reply_markup)

# Handle button clicks
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    selected_option = query.data
    link = OPTIONS_LINKS.get(selected_option, "No link found for this option.")
    await query.answer()
    await query.edit_message_text(f"You selected: {selected_option}\nHere's your link: {link}")

# Main function to run the bot
def main():
    application = Application.builder().token(TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_click))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()