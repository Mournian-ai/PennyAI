from core.event_bus import EventBus
from models.event_models import ChatMessage
import requests

class MemoryService:
    def __init__(self, event_bus: EventBus, settings):
        self.event_bus = event_bus
        self.settings = settings
        self.base_url = self.settings.memory_server_url.rstrip("/")
        self.event_bus.subscribe("chat_message", self.store_message)

    def store_message(self, message: ChatMessage):
        data = {"username": message.user, "context": message.message}
        try:
            requests.post(f"{self.base_url}/store", json=data, timeout=5)
        except Exception as e:
            print(f"Failed to store memory: {e}")

    def query(self, search: str):
        try:
            resp = requests.get(f"{self.base_url}/query", params={"q": search}, timeout=5)
            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            print(f"Memory query failed: {e}")
            return {}
