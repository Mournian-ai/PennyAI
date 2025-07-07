from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ChatMessage(BaseModel):
    user: str
    message: str
    timestamp: datetime

class PennyResponse(BaseModel):
    text: str
    mood: Optional[str] = "neutral"

class TwitchEvent(BaseModel):
    type: str
    data: dict
