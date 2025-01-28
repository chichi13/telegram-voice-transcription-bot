import re


def post_process_text(text):
    """Improves the quality of transcribed text"""
    # Clean up punctuation
    text = re.sub(r"\s+([.,!?])", r"\1", text)
    text = re.sub(r"([.,!?])([^\s\n])", r"\1 \2", text)

    # Capitalize first letter
    text = text.strip()
    if text:
        text = text[0].upper() + text[1:] if len(text) > 1 else text.upper()

    return text
