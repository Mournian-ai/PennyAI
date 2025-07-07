from core.event_bus import EventBus
from models.event_models import ChatMessage
from datetime import datetime
# in future you may add:
# import twitchio

class TwitchChatService:
    def __init__(self, event_bus: EventBus, settings):
        self.event_bus = event_bus
        self.settings = settings
        
    def start(self):
        # placeholder for connecting to Twitch chat
        print("TwitchChatService connected")
