# PennyAI(WIP Wont work unless you setup a Coqui TTS Server, and a ChromaDB with Fast API, can use localhost if all on same machine or could reconfigure to use web sockets)

PennyAI is a prototype Twitch chatbot that uses OpenAI to respond to viewers with a playful personality. It can store conversation history via a memory service and synthesize replies through a TTS server.

## Setup

1. Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate
pip install -r Penny/requirements.txt
```

2. Copy `.env.example` to `.env` and fill in the required values:

```bash
cp .env.example .env
# edit .env with your credentials
```

## Environment Variables

`Penny/core/config.py` expects the following variables:

- `TWITCH_CLIENT_ID` – Twitch application client ID
- `TWITCH_CLIENT_SECRET` – Twitch application client secret
- `TWITCH_BOT_TOKEN` – OAuth token for your bot
- `TWITCH_CHANNEL` – Twitch channel name to join
- `OPENAI_API_KEY` – OpenAI API key
- `TTS_SERVER_URL` – URL to the TTS server
- `MEMORY_SERVER_URL` – URL to the memory server
- `CHROMA_DB_PATH` – path where ChromaDB data is stored (optional)

## Running

Run the main script from the repository root:

```bash
python Penny/main.py
```

The bot will connect to Twitch, handle chat and events, generate responses with OpenAI, and send them to the TTS server.
