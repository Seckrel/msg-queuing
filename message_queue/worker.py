def Worker(item: str):
    """
    Simple Example for worker that processes item from queue.
    In this case, uppercase worker

    Args:
        item (str): pop-ed item from redis queue

    Returns:
        str: Retuns upper-cased str
    """
    return item.upper()
