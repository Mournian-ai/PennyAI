from core.event_bus import EventBus
from models.event_models import PennyResponse
# you will use:
# import requests

class SpeakingService:
    def __init__(self, event_bus: EventBus, settings):
        self.event_bus = event_bus
        self.settings = settings
        self.event_bus.subscribe("speak", self.speak)

    def speak(self, penny_response: PennyResponse):
        # send penny_response.text to your Coqui TTS server
        pass
