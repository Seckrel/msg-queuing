from .message_queue import MessageQueue


async def Producer(data: str, message_queue: MessageQueue):
    """Adds messages to the Redis queue."""
    await message_queue.produce(data)
