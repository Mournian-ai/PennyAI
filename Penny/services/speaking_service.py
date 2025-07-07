from core.event_bus import EventBus
from models.event_models import PennyResponse
import requests

class SpeakingService:
    def __init__(self, event_bus: EventBus, settings):
        self.event_bus = event_bus
        self.settings = settings
        self.event_bus.subscribe("speak", self.speak)

    def speak(self, penny_response: PennyResponse):
        try:
            requests.post(
                self.settings.tts_server_url,
                json={"text": penny_response.text},
                timeout=5,
            )
        except Exception as e:
            print(f"TTS request failed: {e}")
