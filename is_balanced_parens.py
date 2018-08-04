open_chars = '([{'
close_chars = ')]}'
open2closed = dict(zip(open_chars, close_chars))


def is_balanced(string):
    if not string:
        return True

    while string:
        opener = string[0]
        if opener not in open_chars:
            return False
        closer = open2closed[opener]
        if closer not in string:
            return False
        closer_idx = string.index(closer)
        substring = string[1:closer_idx]
        if not is_balanced(substring):
            return False
        string = string[closer_idx + 1:]

    return True
