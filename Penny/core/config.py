from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    # Twitch credentials
    twitch_client_id: str = Field(..., env="TWITCH_CLIENT_ID")
    twitch_client_secret: str = Field(..., env="TWITCH_CLIENT_SECRET")
    twitch_bot_token: str = Field(..., env="TWITCH_BOT_TOKEN")
    twitch_channel: str = Field(..., env="TWITCH_CHANNEL")

    # OpenAI
    openai_api_key: str = Field(..., env="OPENAI_API_KEY")

    # Coqui TTS server
    tts_server_url: str = Field("http://192.168.0.124:7500/tts", env="TTS_SERVER_URL")

    # ChromaDB
    chroma_db_path: str = Field("./chromadb", env="CHROMA_DB_PATH")

    class Config:
        env_file = ".env"
