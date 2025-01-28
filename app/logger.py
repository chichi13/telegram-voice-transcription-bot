import logging

from app.config import settings

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=settings.LOGGING_LEVEL,
)
logger = logging.getLogger(__name__)
