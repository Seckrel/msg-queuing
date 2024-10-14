from redis import Redis

QUEUE_NAME = 'message_q'


def is_queue_empty(queue: Redis) -> bool:
    """
    Checks if redis queue is empty

    Args:
        queue (Redis): redist connected client

    Returns:
        bool: returns true if queue is empty
    """
    global QUEUE_NAME
    return queue.llen(QUEUE_NAME) == 0

