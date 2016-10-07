def d2a(d):
    ab = [2**6 + i for i in [1, 3, 7, 20]]
    w = []
    for n in map(ord, d):
        if n == ab[3]:
            yield chr(int(''.join(map(str, w)), 3))
            w = []
        else:
            w.append(ab.index(n))


def i2n(i, n):
    assert n <= 10
    if not i:
        return '0'
    j = []
    while i:
        i, _j = divmod(i, n)
        j.append(_j)
    return ''.join(map(str, reversed(j)))


def a2d(py):
    ab = [2**6 + i for i in [1, 3, 7, 20]]
    for c in py:
        b3 = map(int, i2n(ord(c), 3))
        for i in b3:
            yield chr(ab[i])
        yield chr(ab[3])
