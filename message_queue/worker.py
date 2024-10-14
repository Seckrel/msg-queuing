import asyncio
from .queue import QUEUE_NAME
from redis import Redis


async def Worker(queue: Redis):
    """
    Perform actions/tasks on queued items

    Args:
        queue (Redis): redis connected client

    Returns:
        str|None: returns processed string or None if queue is empty
    """
    print(f"Queue Size {queue.llen(QUEUE_NAME)}")

    item = queue.blpop(QUEUE_NAME, timeout=5)
    if item:
        # processing | remove this and add actual task to perfom on the queued item
        await asyncio.sleep(3)

        _, message = item
        print(f"Processed {message}")
        return message

    return None
