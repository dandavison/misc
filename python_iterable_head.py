def it():
    for i in [1, 2, 3]:
        print(i)
        yield i



# head, *tail = it()

head = next(iter(it()))
