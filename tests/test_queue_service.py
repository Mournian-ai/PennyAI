import asyncio

from core.event_bus import EventBus
from services.queue_service import QueueService
from models.event_models import PennyResponse


def test_queue_service_processes_responses_sequentially():
    bus = EventBus()
    queue = QueueService(bus)

    spoken = []

    def on_speak(response: PennyResponse):
        spoken.append(response.text)

    async def run_test():
        bus.subscribe("speak", on_speak)

        first = PennyResponse(text="first")
        second = PennyResponse(text="second")

        bus.publish("penny_response", first)
        bus.publish("penny_response", second)

        await asyncio.sleep(0.01)

    asyncio.run(run_test())

    assert spoken == ["first", "second"]
