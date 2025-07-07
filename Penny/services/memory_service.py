from core.event_bus import EventBus
from models.event_models import ChatMessage
# ChromaDB
# from chromadb import Client

class MemoryService:
    def __init__(self, event_bus: EventBus, settings):
        self.event_bus = event_bus
        self.settings = settings
        self.event_bus.subscribe("chat_message", self.store_message)

    def store_message(self, message: ChatMessage):
        # store to chromadb
        pass

    def query(self, user: str):
        # retrieve memories
        pass
