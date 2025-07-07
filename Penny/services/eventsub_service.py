from core.event_bus import EventBus

class EventSubService:
    def __init__(self, event_bus: EventBus, settings):
        self.event_bus = event_bus
        self.settings = settings

    def start(self):
        # you will import twitch API libraries here eventually, eg:
        # from twitchAPI.eventsub.websocket import EventSubWebsocket
        # but leave blank for now
        pass
