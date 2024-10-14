from .queue import QUEUE_NAME
from redis import Redis


async def Producer(message: str, queue: Redis):
    try:
        queue.lpush(QUEUE_NAME, message)
    except:
        import traceback
        traceback.print_exc()
