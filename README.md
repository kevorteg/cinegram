# CineGram Bot

![Python](https://img.shields.io/badge/Python-3.14-blue?style=flat-square&logo=python)
![Telegram](https://img.shields.io/badge/Telegram-Bot_API-blue?style=flat-square&logo=telegram)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-success?style=flat-square)

**Automated Public Domain Movie Publishing Bot for Telegram.**

CineGram autonomously processes video files, extracts metadata, translates synopses, and generates professional posters for Telegram channels.

---

## Architecture & Features

This project utilizes a modular architecture designed for stability and autonomy.

*   **AI Deep Search**: Uses **Local AI** to "read" filenames and captions when standard cleaning fails, handling spam and typos intelligently.
*   **Smart Posters**: Generates cinema-style 16:9 posters with **Blurred Backgrounds** to prevent cropping faces.
*   **Ghost Mode**: Automatically cleans up the chat by deleting user videos and self-destructing status messages after publishing.
*   **Metadata Integration**: Fetches real-time data from **TMDB** (The Movie Database).
*   **AI Translation**: Integrates **Ollama** (running locally) to translate English synopses to Latin American Spanish automatically.
*   **Strict Validation**: Prevents publishing of incomplete content (missing poster or year).
*   **Direct Channel Publishing**: bypasses user forwarding and publishes processed content directly to the configured channel.

## Installation

### Prerequisites
*   Python 3.9+
*   [Ollama](https://ollama.com/) (for AI translation)
*   TMDB API Key

### Setup

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/kevorteg/cinegram.git
    cd cinegram
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configuration**
    Copy `.env.example` to `.env` and populate the variables:
    ```ini
    BOT_TOKEN=your_telegram_bot_token
    CHANNEL_ID=-100xxxxxxxxxx
    TMDB_API_KEY=your_tmdb_key
    # Optional: AI Model Configuration
    OLLAMA_MODEL=dolphin-llama3:latest
    ```

## Usage

1.  **Start the Bot**
    ```bash
    python -m cinegram.bot
    ```

2.  **Interact**
    *   **Forward a Video**: The bot will auto-clean the title, fetch data, translate the synopsis, and publish to the channel.
    *   **Search**: Use `/search Movie Name` to find content manualy.
    *   **Links**: Send an Internet Archive link to process it.

## Development

**Project Structure:**
```text
cinegram/
├── bot.py                  # Entry Point
├── config/                 # Settings & Environment
├── handlers/               # Command & Message Handlers
├── services/               # Core Logic (TMDB, Ollama, ImageGen)
└── utils/                  # Helper functions
```

## Contact & Ideas

Have a bot idea? Interested in custom automation?

**Contact me on Telegram:** [@KrimsonByte](https://t.me/KrimsonByte)

---
*Built with precision. No bloat.*
