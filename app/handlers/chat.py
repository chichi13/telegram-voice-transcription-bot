from telegram import ChatMemberUpdated, Update
from telegram.constants import ChatMemberStatus
from telegram.ext import ContextTypes

from app.logger import logger
from app.state import authorized_groups


def extract_status_change(
    chat_member_update: ChatMemberUpdated,
) -> tuple[bool, bool] | None:
    """Extracts whether the user was a chat member and whether they are now."""

    old_is_member = chat_member_update.old_chat_member.status in [
        ChatMemberStatus.MEMBER,
        ChatMemberStatus.OWNER,
        ChatMemberStatus.ADMINISTRATOR,
    ]
    new_is_member = chat_member_update.new_chat_member.status in [
        ChatMemberStatus.MEMBER,
        ChatMemberStatus.OWNER,
        ChatMemberStatus.ADMINISTRATOR,
    ]
    return old_is_member, new_is_member


async def track_chats(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Tracks chat member status changes."""

    result = extract_status_change(update.my_chat_member)

    if result is None:
        return

    was_member, is_member = result

    chat = update.effective_chat
    if chat.type in ["group", "supergroup"]:
        if not was_member and is_member:
            logger.info(f"Bot added to group {chat.id}")
            authorized_groups.add(chat.id)
            await context.bot.send_message(
                chat_id=chat.id,
                text="👋 Hello! I am ready to transcribe voice messages in this group.",
            )
        elif was_member and not is_member:
            logger.info(f"Bot removed from group {chat.id}")
            authorized_groups.discard(chat.id)
