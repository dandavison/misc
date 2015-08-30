from contextlib import contextmanager
from django.db import connection
from django.db import transaction


def max_queries(n, trace=True):
    from functools import wraps
    from django.db import connection
    from clint.textui.colored import red as col

    def _max_queries(func):

        def __max_queries(*args, **kwargs):
            q0 = len(connection.queries)
            ret = func(*args, **kwargs)
            q1 = len(connection.queries)
            if trace:
                print col("%s: %d queries" % (func.__name__, q1 - q0))
            if q1 - q0 > n:
                raise AssertionError("%d queries in %s" % (
                    q1 - q0,
                    func.__name__,
                ))
            return ret

        return wraps(func)(__max_queries)

    return _max_queries


def print_queries(func):
    from functools import wraps
    from django.db import connection
    from clint.textui.colored import green as col

    def _print_queries(*args, **kwargs):
        q0 = len(connection.queries)
        ret = func(*args, **kwargs)
        q1 = len(connection.queries)
        print col("%s: %d queries" % (func.__name__, q1 - q0))
        return ret

    return wraps(func)(_print_queries)


@contextmanager
def rollback():
    """
    Run statements in a transaction and do not commit.
    """
    if transaction.is_managed():
        raise RuntimeError("May not be run in a transaction")
    class Rollback(Exception):
        pass
    try:
        with transaction.commit_on_success():
            yield
            raise Rollback()
    except Rollback:
        pass


def trace(func):
    from functools import wraps
    from django.db import connection

    def _print_queries(*args, **kwargs):
        q0 = len(connection.queries)
        ret = func(*args, **kwargs)
        q1 = len(connection.queries)
        print "%s(%s, %s): %d queries" % (
            func.__name__,
            args,
            kwargs,
            q1 - q0,
        )
        return ret

    return wraps(func)(_print_queries)



# challenge: This prints the current function name
# Write a metaclass that
# import inspect
# print col(inspect.stack()[0][3])
