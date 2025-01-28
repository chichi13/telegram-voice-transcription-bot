import os

from pydub import AudioSegment

from app.config import settings
from app.services.audio import clean_audio
from app.state import whisper_model


async def transcribe_voice(voice_path: str, wav_path: str):
    """Transcribes a voice file"""

    try:
        audio = AudioSegment.from_ogg(voice_path)
        audio = clean_audio(audio)
        audio.export(wav_path, format="wav")

        result = whisper_model.transcribe(
            wav_path,
            language=settings.AUDIO_LANGUAGE,
            beam_size=5,
            word_timestamps=True,
            initial_prompt=settings.AUDIO_INITIAL_PROMPT,
            temperature=0.0,
            vad_filter=True,
        )
        return result
    finally:
        # Cleanup files
        if os.path.exists(voice_path):
            os.remove(voice_path)
        if os.path.exists(wav_path):
            os.remove(wav_path)
