from core.event_bus import EventBus
from models.event_models import ChatMessage
from datetime import datetime
from twitchio.ext import commands
import threading
import logging

logger = logging.getLogger(__name__)

class TwitchChatService(commands.Bot):
    def __init__(self, event_bus: EventBus, settings):
        self.event_bus = event_bus
        self.settings = settings
        super().__init__(
            token=self.settings.twitch_bot_token,
            prefix="!",
            initial_channels=[self.settings.twitch_channel],
        )
        self.event_bus.subscribe("chat_reply", self._send_message)

    def start(self):
        threading.Thread(target=self.run, daemon=True).start()

    async def event_ready(self):
        logger.info("TwitchChatService connected as %s", self.nick)

    async def event_message(self, message):
        if message.echo:
            return
        chat = ChatMessage(
            user=message.author.name,
            message=message.content,
            timestamp=datetime.utcnow(),
        )
        self.event_bus.publish("chat_message", chat)

    async def _send_message(self, text: str):
        chan = self.get_channel(self.settings.twitch_channel)
        if chan:
            await chan.send(text)

