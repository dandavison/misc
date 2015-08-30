from contextlib import contextmanager


@contextmanager
def context_manager_test():
    print 'before'
    try:
        yield
    finally:
        print 'after'


with context_manager_test():
    print 'hello'
    raise Exception
