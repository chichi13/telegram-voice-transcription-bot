from pydantic_settings import BaseSettings


class Config(BaseSettings):
    LOGGING_LEVEL: str = "INFO"
    WHISPER_MODEL: str = "large-v3"
    WHISPER_DEVICE: str = "cpu"
    WHISPER_COMPUTE_TYPE: str = "int8"
    AUDIO_LANGUAGE: str = "fr"
    AUDIO_INITIAL_PROMPT: str = "Transcription of a French voice message."

    TELEGRAM_BOT_TOKEN: str


settings = Config(_env_file=".env", _env_file_encoding="utf-8")
