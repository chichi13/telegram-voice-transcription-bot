# Telegram Voice Transcription Bot

A Telegram bot that automatically transcribes voice messages into text using OpenAI's Whisper model.

## Features

- Automatic transcription of voice messages to text
- Support for both groups and private conversations
- Automatic activation when added to a group
- Automatic cleanup of temporary files
- Audio quality optimization before transcription

## Prerequisites

- Python 3.11+
- FFmpeg
- A Telegram bot token (obtained from [@BotFather](https://t.me/botfather))

## Installation

### Using Docker (recommended)

1. Clone the repository:

```bash
git clone https://github.com/[your-username]/telegram-voice-transcription-bot.git
cd telegram-voice-transcription-bot
```

2. Configure your Telegram token in `config.py` or via environment variable

3. Build and run the container:

```bash
docker build -t voice-transcription-bot .
docker run -d voice-transcription-bot
```

### Manual Installation

1. Clone the repository:

```bash
git clone https://github.com/[your-username]/telegram-voice-transcription-bot.git
cd telegram-voice-transcription-bot
```

2. Install dependencies:

```bash
pip install -r requirements/dev.txt
# Or for production
pip install -r requirements/prod.txt
```

3. Install FFmpeg:
- On Debian/Ubuntu:
  ```bash
  sudo apt-get install ffmpeg
  ```
- On macOS:
  ```bash
  brew install ffmpeg
  ```

4. Configure your environment:
   - Create a `.env` file in the project root directory
   - Add your Telegram bot token:
     ```bash
     TELEGRAM_BOT_TOKEN=your-token-here

     LOGGING_LEVEL=INFO # Logging level (DEBUG, INFO, WARNING, ERROR)
     WHISPER_MODEL=large-v3 # Model name (large-v3, base, etc.)
     WHISPER_DEVICE=cpu # Device (cpu, cuda)
     WHISPER_COMPUTE_TYPE=int8 # Compute type (int8, fp16, fp32)
     
     AUDIO_LANGUAGE=fr # Language code (en, fr, es, etc.)
     AUDIO_INITIAL_PROMPT=Transcription of a French voice message. # Initial prompt for Whisper
     ```

5. Run the bot:

```bash
python main.py
```

## Usage

1. Start a private conversation with the bot or add it to a group

2. In private conversation:
   - Send a voice message
   - The bot will automatically transcribe the message

3. In group:
   - Add the bot to the group
   - The bot activates automatically
   - Send a voice message
   - The bot will reply with the transcription

## Technologies Used

- [python-telegram-bot](https://python-telegram-bot.org/) - Framework for Telegram bots
- [faster-whisper](https://github.com/guillaumekln/faster-whisper) - Optimized implementation of Whisper
- [pydub](https://github.com/jiaaro/pydub) - Audio manipulation
