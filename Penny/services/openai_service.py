from core.event_bus import EventBus
from models.event_models import ChatMessage, PennyResponse
# import openai

class OpenAIService:
    def __init__(self, event_bus: EventBus, settings):
        self.event_bus = event_bus
        self.settings = settings
        self.event_bus.subscribe("chat_message", self.generate_reply)

    def generate_reply(self, chat_message: ChatMessage):
        # call OpenAI
        # self.event_bus.publish("penny_response", PennyResponse(text="Hi!"))
        pass
