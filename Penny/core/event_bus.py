# core/event_bus.py

from collections import defaultdict
import asyncio
import inspect

class EventBus:
    def __init__(self):
        self._subscribers = defaultdict(list)

    def subscribe(self, event_name, callback):
        self._subscribers[event_name].append(callback)

    def publish(self, event_name, data=None):
        for callback in self._subscribers[event_name]:
            if inspect.iscoroutinefunction(callback):
                asyncio.create_task(callback(data))
            else:
                callback(data)
