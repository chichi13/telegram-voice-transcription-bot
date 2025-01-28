from telegram import Update
from telegram.ext import ContextTypes

from app.logger import logger
from app.services.whisper import transcribe_voice
from app.state import authorized_groups
from app.utils.text import post_process_text


async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles voice message reception"""

    chat_id = update.effective_chat.id
    chat_type = update.effective_chat.type

    logger.info(f"Voice message received - Chat ID: {chat_id}")

    if chat_type in ["group", "supergroup"] and chat_id not in authorized_groups:
        logger.warning(f"Unauthorized group: {chat_id}")
        return

    try:
        message = await update.message.reply_text("📝 Transcription in progress...")

        voice = update.message.voice
        voice_file = await context.bot.get_file(voice.file_id)

        file_name = f"temp_voice_{update.message.message_id}"
        voice_path = f"{file_name}.ogg"
        wav_path = f"{file_name}.wav"

        await voice_file.download_to_drive(voice_path)

        transcription_result = await transcribe_voice(voice_path, wav_path)

        # Combine segments into text
        text = " ".join(segment.text for segment in transcription_result[0])
        final_text = post_process_text(text)

        try:
            await message.delete()
        except Exception:
            pass

        sender_name = update.message.from_user.first_name
        response_text = (
            f"🎙️ Voice message from {sender_name}:\n"
            f"📝 Transcription:\n\n{final_text}"
        )

        await update.message.reply_text(
            response_text, reply_to_message_id=update.message.message_id
        )

    except Exception as e:
        logger.error(f"Error during transcription: {str(e)}", exc_info=True)
        try:
            await update.message.reply_text(
                f"❌ Sorry, an error occurred during transcription: {str(e)}"
            )
        except Exception as reply_error:
            logger.error(f"Unable to send error message: {reply_error}")
