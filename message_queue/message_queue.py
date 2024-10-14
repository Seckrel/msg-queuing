from redis import Redis
import asyncio
from timeit import default_timer

class MessageQueue:
    def __init__(
        self,
        redis_client: Redis,
        queue_name="message_1",
        worker=None,
        verbose=False,
        *args,
        **kwargs,
    ) -> None:
        self.redis_client = redis_client
        self.queue_name = queue_name

        self.worker = worker
        self.verbose = verbose
        self.args = args
        self.kwargs = kwargs

    def qsize(self):
        return self.redis_client.llen(self.queue_name)

    async def produce(self, message: str):
        """Pushes a message to the Redis queue."""
        self.redis_client.rpush(self.queue_name, message)

        if self.verbose:
            print(f"Message '{message}' added to queue {self.queue_name}")

    async def consume(self):
        """Waits for a message from the Redis queue."""
        s = default_timer()
        item = self.redis_client.blpop(self.queue_name, timeout=5)
        print("time", default_timer() - s)
        if self.verbose:
            print(f"Queue Size {self.qsize()}")

        if not item:
            return None

        _, message = item

        if self.worker:
            message = self.worker(message)

        if self.verbose:
            print(f"Processed {message}")

        return message
