#!/usr/bin/env python2

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
    j = []
    while i:
        i, _j = divmod(i, n)
        j.append(_j)
    return ''.join(map(str, reversed(j or [0])))


def a2d(py):
    ab = [2**6 + i for i in [1, 3, 7, 20]]
    for c in py:
        b3 = map(int, i2n(ord(c), 3))
        for i in b3:
            yield chr(ab[i])
        yield chr(ab[3])


T = '''
from a2d import d2a
exec d2a("""
%s
""")
'''.lstrip()


def formatted(s):
    from more_itertools import chunked
    for chunk in chunked(s, 79):
        yield ''.join(chunk)
        yield '\n'


if __name__ == '__main__':
    import sys
    m, f = sys.argv[1:]

    if m == 'o':
        with open(f) as fi:
            a = fi.read()
            if not a.strip():
                sys.exit(0)
        with open(f, 'w') as fo:
            fo.write(T % ''.join(formatted(a2d(a))).strip())
    elif m == 'i':
        with open(f) as fi:
            sys.stdout.write(''.join(d2a(fi.read())))
