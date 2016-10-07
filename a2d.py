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
    from math import ceil, log
    k = int(ceil(log(i + 1, n)) + 1)
    j = []
    while k + 1:
        _j, i = divmod(i, n ** k)
        j.append(_j)
        k -= 1
    return str(int(''.join(map(str, j))))


def a2d(py):
    ab = [2**6 + i for i in [1, 3, 7, 20]]
    for c in py:
        b3 = map(int, i2n(ord(c), 3))
        for i in b3:
            yield chr(ab[i])
        yield chr(ab[3])
