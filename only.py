def only(iterable):
    """
    Return the only element of the iterable.
    """
    iterator = iter(iterable)
    try:
        val = next(iterator)
    except StopIteration:
        raise ValueError("The iterable is empty")
    try:
        next(iterator)
        raise ValueError("The iterable contains more than one element")
    except StopIteration:
        return val
