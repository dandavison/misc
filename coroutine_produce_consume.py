def produce():
    while True:
        while queue is not full:
            create items
            add items to queue
        consume()


def consume():
    while True:
        while queue is not empty:
            remove items
            use items
        produce()
