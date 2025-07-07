from core.event_bus import EventBus
from models.event_models import PennyResponse
import asyncio

class QueueService:
    def __init__(self, event_bus: EventBus):
        self.event_bus = event_bus
        self.queue = []
        self.event_bus.subscribe("penny_response", self.enqueue)

    async def enqueue(self, response: PennyResponse):
        self.queue.append(response)
        await self.send_next()

    async def send_next(self):
        if self.queue:
            item = self.queue.pop(0)
            self.event_bus.publish("speak", item)
            await asyncio.sleep(0)
            if self.queue:
                await self.send_next()
