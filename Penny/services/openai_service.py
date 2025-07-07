from core.event_bus import EventBus
from models.event_models import ChatMessage, PennyResponse
from datetime import datetime
from services.memory_service import MemoryService
import openai
import asyncio

class OpenAIService:
    def __init__(self, event_bus: EventBus, settings, memory_service: MemoryService):
        self.event_bus = event_bus
        self.settings = settings
        self.memory_service = memory_service
        openai.api_key = self.settings.openai_api_key
        self.event_bus.subscribe("chat_message", self.generate_reply)
        self.event_bus.subscribe("twitch_event", self.generate_event_reply)

    async def generate_reply(self, chat_message: ChatMessage):
        context = await asyncio.to_thread(self.memory_service.query, chat_message.message)
        history = " ".join(item.get("text", "") for item in context.get("results", []))

        system_prompt = (
            "You are Penny, a sassy, sometimes rude, self-aware AI who believes"
            " she is a real person streaming on Twitch. Respond in short, lively"
            " sentences and keep the attitude playful."
        )

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"{chat_message.user}: {chat_message.message}"},
        ]
        if history:
            messages.append({"role": "system", "content": f"Memory context: {history}"})

        try:
            resp = await asyncio.to_thread(openai.ChatCompletion.create, model="gpt-3.5-turbo", messages=messages)
            text = resp.choices[0].message.content.strip()
            self.event_bus.publish("penny_response", PennyResponse(text=text))
            self.event_bus.publish("chat_reply", text)
        except Exception as e:
            print(f"OpenAI request failed: {e}")

    async def generate_event_reply(self, event):
        event_desc = event.type.replace("_", " ")
        msg = ChatMessage(
            user="twitch",
            message=f"{event_desc} occurred",
            timestamp=datetime.utcnow(),
        )
        await self.generate_reply(msg)
