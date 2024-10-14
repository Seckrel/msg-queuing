from redis import Redis
from fastapi import WebSocket
import asyncio


class MessageQueue:
    def __init__(
        self,
        redis_client: Redis,
        websocket: WebSocket,
        channel_name="message_1",
        worker=None,
        verbose=False,
        *args,
        **kwargs,
    ) -> None:
        self.redis_client = redis_client
        self.ws = websocket
        self.channel_name = channel_name
        self.pubsub = self.redis_client.pubsub()

        self.worker = worker
        self.verbose = verbose
        self.args = args
        self.kwargs = kwargs

    def qsize(self):
        return self.redis_client.llen(self.channel_name)

    def unsubscribe(self):
        """UnSubscribe channel from redis pubsub"""
        self.pubsub.unsubscribe(self.channel_name)

    async def produce(self, message: str):
        """Pushes a message to the Redis queue."""
        # self.redis_client.rpush(self.channel_name, message)
        self.redis_client.publish(self.channel_name, message)

        if self.verbose:
            print(f"Message '{message}' published to {self.channel_name}")

    async def consume(self):
        """Waits for a message from the Redis queue."""
        self.pubsub.subscribe(self.channel_name)

        try:
            while True:
                message = self.pubsub.get_message(ignore_subscribe_messages=True)

                if message:
                    data = message["data"]

                    if self.worker:
                        data = self.worker(data)

                    if self.verbose:
                        print(f"Processed {data}")

                    await self.ws.send_text(data)
                await asyncio.sleep(
                    0.1
                )  # Sleep briefly to yield control and avoid busy-waiting

        except Exception as e:
            if self.verbose:
                print(f"Error in consuming messages: {e}")

        finally:
            self.unsubscribe()
