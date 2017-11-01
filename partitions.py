def encode(partition):
    """
    Encode list-of-lists partition as an integer.

    `partition` is a list of lists, representing a set partition. The
    elements of the set must be {0, 1, ..., N}.

    Partitions of a set with cardinality N are mapped on to the
    integers 0, 1, ..., C(N)

    where C(N) = sum_{i=1}^{n-1} (n-i)n^{i-1}

    So the largest integer code for sets of cardinality 4 is 27,
    i.e. 123 in base 4.

    >>> partition = [[0], [1, 2, 3]]
    >>> encode(partition)
    21
    """
    # Construct a sequence of integers (K_1, K_2, ...) where K_i == k
    # means that the ith element of the set is in the kth part (a
    # 'part' is a set and a 'partition' is a set of 'parts'). Treat
    # that sequence of integers as a base C integer, where C is the
    # cardinality of the set.
    code = {}
    cardinality = 0
    for part in partition:
        if not part:
            continue
        key = min(part)
        for elem in part:
            code[elem] = key
            cardinality += 1

    if not cardinality > 1:
        return 0
    else:
        code = ''.join(str(val) for key, val in sorted(code.iteritems()))
        return int(code, cardinality)


def decode(code, cardinality):
    """
    Return list-of-lists partition encoded by `code`.

    >>> partition = [[0], [1, 2, 3]]
    >>> decode(encode(partition), 4)
    [[0], [1, 2, 3]]
    """
    if cardinality == 0:
        return []
    elif cardinality == 1:
        return [[0]]

    code = to_base(code, cardinality)
    code = map(int, pad(code, cardinality))

    partition = {}
    for i, val in enumerate(code):
        partition.setdefault(val, []).append(i)

    return sorted(partition.values())


def pad(s, k):
    """
    Left-pad string with zeros up to length k.
    """
    padded = ['0'] * k
    padded[-len(s):] = list(s)
    return ''.join(padded)


def to_base(n, base):
    """
    Convert integer to base `base` string representation.

    >>> to_base(27, 4)
    '123'
    >>> to_base(0, 4)
    '0'
    """
    assert base > 1
    nn = []
    while n > 0:
        n, remainder = divmod(n, base)
        nn.append(remainder)

    if not nn:
        return '0'
    else:
        return ''.join(map(str, nn[::-1]))


def test_partition(partition):
    cardinality = sum(map(len, partition))
    assert decode(encode(partition), cardinality) == partition


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    for partition in [
            [],
            [[0]],
            [[0, 1]],
            [[0], [1]],
            [[0, 1], [2]],
            [[0, 1], [2, 3]],
            [[0, 1, 4], [2, 3]],
            [[0, 1, 4], [2, 3, 5]],
    ]:
        print partition
        test_partition(partition)
