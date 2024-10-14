# FastAPI Message Queuing System w/ Redis and WebSockets 📩 📨 📤

## Table of Content
- [Introduction](#Introduction)
    - [Key Feature](#Key-Feature)
    - [How it Works](#How-it-Works)
- [How to Run](#How-to-Run)
    - [Requirements](#Requirements)
    - [Initial Setup](#Initial-Setup)
- [Run Project](#Run-Project)

# Introduction
This project implements a message queuing system built with FastAPI, Redis, and WebSockets. The system allows asynchronous communication between producers (clients sending messages) and consumers (workers processing messages) using Redis as the message broker and WebSockets for real-time communication.

## Key Feature
- **Producer-Consumer Architecture:** The system follows a classic producer-consumer model where messages are produced and consumed asynchronously using Redis.
- **Redis Queue:** Redis is used to implement a queue where messages are stored and processed in a First-In, First-Out (FIFO) order.
- **WebSocket Communication:** Real-time bidirectional communication between the client and the server is handled using WebSockets, allowing for immediate updates once messages are processed.
- **Asynchronous Processing:** FastAPI’s asynchronous capabilities allow for scalable and non-blocking processing of messages, making the system suitable for high-performance use cases.

## How it Works
1. **Producers:** Clients connect via WebSocket and send messages to the server.
2. **Redis Queue:** Messages are pushed into a Redis queue. Redis acts as a broker, holding the messages until they are consumed.# FastAPI Message Queuing System w/ Redis and WebSockets 📩 📨 📤

## Table of Content
- [Introduction](#Introduction)
    - [Branches](#Branches)
    - [Key Feature](#Key-Feature)
    - [How it Works](#How-it-Works)
- [How to Run](#How-to-Run)
    - [Requirements](#Requirements)
    - [Initial Setup](#Initial-Setup)
- [Run Project](#Run-Project)

# Introduction
This project implements a message queuing system built with FastAPI, Redis, and WebSockets. The system allows asynchronous communication between producers (clients sending messages) and consumers (workers processing messages) using Redis as the message broker and WebSockets for real-time communication.

## Branches
- [main](https://github.com/Seckrel/simple-msg-queuing): Implements Message Queuing using Redis Pub/Sub
- [redis-queue](https://github.com/Seckrel/simple-msg-queuing/tree/redis-queue): Implements Message Queuing using Redis Queue

#### ⚠️ These are two different branches of this repo.

## Key Feature
- **Producer-Consumer Architecture:** The system follows a classic producer-consumer model where messages are produced and consumed asynchronously using Redis.
- **Redis Queue:** Redis is used to implement a queue where messages are stored and processed in a First-In, First-Out (FIFO) order.
- **Redis Pub/Sub**: Implements a real-time messaging system where published messages are instantly delivered to active subscribers without being stored. It’s ideal for broadcasting but lacks message persistence and delivery guarantees.
- **WebSocket Communication:** Real-time bidirectional communication between the client and the server is handled using WebSockets, allowing for immediate updates once messages are processed.
- **Asynchronous Processing:** FastAPI’s asynchronous capabilities allow for scalable and non-blocking processing of messages, making the system suitable for high-performance use cases.

## How it Works
### Redis Pub/Sub
1. **Producers:** Clients connect via WebSocket and send messages to the server.
2. **Redis Pub/Sub:** Messages are published to a Redis channel, and Redis acts as a broker, instantly delivering messages to all active subscribers.
3. **Consumers (Subscribers):** The system includes subscribers that listen to the Redis channel, process the messages in real-time, and handle the result.
4. **WebSocket Notifications:** Once a message is processed, the result is sent back to the client through WebSocket in real-time.

### Redis Queue
1. **Producers:** Clients connect via WebSocket and send messages to the server.
2. **Redis Queue:** Messages are pushed into a Redis queue. Redis acts as a broker, holding the messages until they are consumed.
3. **Consumers (Workers):** The system includes workers that pull tasks from the Redis queue, process them, and return the result.
4. **WebSocket Notifications:** Once a message is processed, the result is sent back to the client through WebSocket in real-time.

# How to Run
## Requirements
- [python@3.11](https://www.python.org/downloads/release/python-31110/)
- [redis](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/)
## Initial Setup
```
python -m venv venv
source ./venv/bin/activate
```

# Run Project
`Run FastAPI Command`


3. **Consumers (Workers):** The system includes workers that pull tasks from the Redis queue, process them, and return the result.
4. **WebSocket Notifications:** Once a message is processed, the result is sent back to the client through WebSocket in real-time.

# How to Run
## Requirements
- [python@3.11](https://www.python.org/downloads/release/python-31110/)
- [redis](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/)
## Initial Setup
```
python -m venv venv
source ./venv/bin/activate
```

# Run Project
`Run FastAPI Command`

