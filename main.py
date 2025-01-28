from telegram.ext import Application, MessageHandler, CommandHandler, ChatMemberHandler, filters
from telegram import Update
from app.logger import logger
from app.config import settings
from app.handlers.voice import handle_voice
from app.handlers.commands import start_command
from app.handlers.chat import track_chats

def main():
    try:
        # Configure the application
        app = Application.builder().token(settings.TELEGRAM_BOT_TOKEN).build()

        # Add handlers
        app.add_handler(MessageHandler(filters.VOICE, handle_voice))
        app.add_handler(CommandHandler("start", start_command))
        app.add_handler(
            ChatMemberHandler(track_chats, ChatMemberHandler.MY_CHAT_MEMBER)
        )

        logger.info("🤖 Bot started! Press Ctrl+C to stop.")

        # Start the Telegram bot
        app.run_polling(allowed_updates=Update.ALL_TYPES)

    except KeyboardInterrupt:
        logger.info("\n🛑 Bot stopping...")
    except Exception as e:
        logger.error(f"Error while starting the bot: {e}", exc_info=True)

if __name__ == "__main__":
    main()