def f(*args, a=True):
    print(args)
    print(a)


def make(*args, replace=True):
    print(args)
    print(replace)


def g(*args, /, final):
    print("args: ", args)
    print("final: ", final)


g(1, 2, 3)
