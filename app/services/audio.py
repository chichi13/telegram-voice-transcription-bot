from pydub.effects import normalize


def clean_audio(audio_segment):
    """Improves audio quality"""

    audio = normalize(audio_segment)
    if audio.channels > 1:
        audio = audio.set_channels(1)
    audio = audio.set_frame_rate(16000)
    audio = audio.low_pass_filter(3000)

    return audio
