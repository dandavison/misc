def g():
    for i in [1, 2]:
        if True:
            continue
        yield i

print list(g())        
