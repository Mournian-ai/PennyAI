import asyncio

from core.event_bus import EventBus


def test_event_bus_publish_and_receive():
    bus = EventBus()
    received_sync = []
    received_async = []

    def sync_callback(data):
        received_sync.append(data)

    async def async_callback(data):
        received_async.append(data)

    async def run_test():
        bus.subscribe("sync_event", sync_callback)
        bus.subscribe("async_event", async_callback)

        bus.publish("sync_event", "hello")
        bus.publish("async_event", "world")

        await asyncio.sleep(0)

    asyncio.run(run_test())

    assert received_sync == ["hello"]
    assert received_async == ["world"]
