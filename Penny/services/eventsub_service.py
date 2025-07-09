from core.event_bus import EventBus
from models.event_models import TwitchEvent
from twitchAPI.twitch import Twitch
from twitchAPI.eventsub.websocket import EventSubWebsocket
import asyncio

class EventSubService:
    def __init__(self, event_bus: EventBus, settings):
        self.event_bus = event_bus
        self.settings = settings
        self.twitch = Twitch(self.settings.twitch_client_id, self.settings.twitch_client_secret)
        self.eventsub = None
        self.channel_id = None

    async def start(self):
        await self.twitch.authenticate_app([])
        await self.twitch.set_user_authentication(self.settings.twitch_bot_token, [], None)
        user = None
        async for u in self.twitch.get_users(logins=[self.settings.twitch_channel]):
            user = u
            break
        if user is None:
            print("Could not resolve Twitch channel ID")
            return
        self.channel_id = user.id
        self.eventsub = EventSubWebsocket(self.twitch)
        await self.eventsub.listen_channel_follow_v2(self.channel_id, self._on_follow)
        await self.eventsub.listen_channel_subscribe(self.channel_id, self._on_sub)
        await self.eventsub.listen_channel_subscription_gift(self.channel_id, self._on_sub_gift)
        await self.eventsub.listen_channel_raid(self.channel_id, self._on_raid)
        await self.eventsub.listen_hype_train_begin(self.channel_id, self._on_hype_begin)
        await self.eventsub.listen_hype_train_progress(self.channel_id, self._on_hype_progress)
        await self.eventsub.listen_hype_train_end(self.channel_id, self._on_hype_end)
        self.eventsub.start()
        print("EventSubService started - listening for events")

    async def _dispatch(self, event_type: str, data):
        self.event_bus.publish("twitch_event", TwitchEvent(type=event_type, data=data.to_dict()))

    async def _on_follow(self, data):
        await self._dispatch("follow", data)

    async def _on_sub(self, data):
        await self._dispatch("subscribe", data)

    async def _on_sub_gift(self, data):
        await self._dispatch("sub_gift", data)

    async def _on_raid(self, data):
        await self._dispatch("raid", data)

    async def _on_hype_begin(self, data):
        await self._dispatch("hype_train_begin", data)

    async def _on_hype_progress(self, data):
        await self._dispatch("hype_train_progress", data)

    async def _on_hype_end(self, data):
        await self._dispatch("hype_train_end", data)
