from fastapi import FastAPI, WebSocket, Depends
from fastapi.responses import HTMLResponse
from .message_queue.producer import Producer
from .message_queue.consumer import Consumer
import asyncio
import redis
from .config.load_redis import pool
from .message_queue.message_queue import MessageQueue
from .message_queue.worker import Worker


app = FastAPI()


def get_redis():
    return redis.Redis(connection_pool=pool)


html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def message_queuing(
    websocket: WebSocket, redis_client: redis.Redis = Depends(get_redis)
):
    """
    Message queuing End-point

    Args:
        websocket (WebSocket): fastapi websocket client
        queue (redis.Redis, optional): connected redis client. Defaults to Depends(get_redis).
    """
    await websocket.accept()

    # Create a MessageQueue instance
    message_queue = MessageQueue(redis_client, websocket, worker=Worker, verbose=True)

    # Start the consumer in a separate task
    asyncio.create_task(message_queue.consume())

    # Producer loop for WebSocket incoming messages
    try:
        while True:
            # Receive text data from WebSocket client
            data = await websocket.receive_text()

            # Publish data to redis pub
            await message_queue.produce(data)

    except Exception as e:
        print(f"WebSocket connection error: {e}")
    finally:
        print("socket closed")
        await websocket.close()
