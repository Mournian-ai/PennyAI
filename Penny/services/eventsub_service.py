from core.event_bus import EventBus

class EventSubService:
    def __init__(self, event_bus: EventBus, settings):
        self.event_bus = event_bus
        self.settings = settings

    def start(self):
        # placeholder for Twitch EventSub integration
        print("EventSubService started - listening for events")
