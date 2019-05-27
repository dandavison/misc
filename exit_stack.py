from contextlib import contextmanager
from contextlib import ExitStack



@contextmanager
def stack_context_managers(*managers):
    with ExitStack() as stack:
        yield [stack.enter_context(manager) for manager in managers]


@contextmanager
def ctx_1():
    print('1.0')
    yield
    print('1.1')


@contextmanager
def ctx_2():
    print('2.0')
    yield
    print('2.1')


with stack_context_managers(ctx_1(), ctx_2()):
    print('3.0')
