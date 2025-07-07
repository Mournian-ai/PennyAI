from core.event_bus import EventBus
from services.eventsub_service import EventSubService
from services.twitch_chat_service import TwitchChatService
from services.memory_service import MemoryService
from services.openai_service import OpenAIService
from services.queue_service import QueueService
from services.speaking_service import SpeakingService
from core.config import Settings

from models.event_models import ChatMessage
import datetime
import asyncio


async def main():
    event_bus = EventBus()
    settings = Settings()
    eventsub = EventSubService(event_bus, settings)
    twitch_chat = TwitchChatService(event_bus, settings)
    memory = MemoryService(event_bus, settings)
    openai = OpenAIService(event_bus, settings, memory)
    queue = QueueService(event_bus)
    speaking = SpeakingService(event_bus, settings)

    await eventsub.start()
    twitch_chat.start()

    # dry test
    test_msg = ChatMessage(user="tester", message="Hey Penny!", timestamp=datetime.datetime.now())
    event_bus.publish("chat_message", test_msg)

    while True:
        await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())
