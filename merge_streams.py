def merge(stream1, stream2):
    sentinel = object()
    stream1, stream2 = iter(stream1), iter(stream2)
    while True:
        x1, x2 = next(stream1, sentinel), next(stream2, sentinel)
        xs = sorted(x for x in [x1, x2] if x is not sentinel)
        if xs:
            for x in xs:
                yield x
        else:
            break


if __name__ == '__main__':
    print(list(merge([], [])))
    print(list(merge([], [2,4,6])))
    print(list(merge([1,3,5], [2,4,6])))
