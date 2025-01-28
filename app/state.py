from faster_whisper import WhisperModel

from app.config import settings
from app.logger import logger

authorized_groups = set()

# Immediate model initialization on import
logger.info("Initializing Whisper model...")
whisper_model = WhisperModel(
    settings.WHISPER_MODEL,
    device=settings.WHISPER_DEVICE,
    compute_type=settings.WHISPER_COMPUTE_TYPE,
    local_files_only=False,
)
logger.info("Whisper model initialized!")
