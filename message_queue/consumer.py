from .worker import Worker
from fastapi import WebSocket
import asyncio
from redis import Redis


async def Consumer(websocket: WebSocket, queue: Redis):
    """
    Consumes items from the message queue

    Args:
        websocket (WebSocket): wb connection to return message
        queue (Redis): redis client
    """
    while True:
        output = await Worker(queue)
        if output:
            await websocket.send_text(f"Message text was: {output}")

        else:
            await asyncio.sleep(1)
