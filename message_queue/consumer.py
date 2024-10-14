from fastapi import WebSocket
import asyncio
from .message_queue import MessageQueue


async def Consumer(websocket: WebSocket, message_queue: MessageQueue):
    """Continuously consumes messages from the Redis queue and sends them to the websocket."""
    while True:
        output = await message_queue.consume()
        if output:
            await websocket.send_text(f"Message text was: {output}")
        else:
            await asyncio.sleep(.5)
