from telegram import Update

from app.logger import logger
from app.state import authorized_groups


async def start_command(update: Update):
    """Handles the /start command"""

    chat_id = update.effective_chat.id
    chat_type = update.effective_chat.type

    if chat_type == "private":
        await update.message.reply_text(
            "👋 Hello! I am a voice transcription bot.\n"
            "You can also add me to your groups!"
        )
    else:
        # For groups, add the group to authorized groups
        authorized_groups.add(chat_id)
        logger.info(f"Group {chat_id} added to authorized groups via /start")
        await update.message.reply_text("✅ The bot is now activated in this group!")
