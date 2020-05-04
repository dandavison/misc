import inspect


def f():
    var = 'val'
    frame = inspect.currentframe()
    print(frame.f_code.co_name)

l = lambda: print(inspect.currentframe().f_code.co_name)

frame = inspect.currentframe()
print(frame.f_code.co_name)
import ipdb ; ipdb.set_trace()
f()
l()
