#!/usr/bin/env python2

def get_exception_message(exception):
    """
    Python 3 removed the .message attribute from the `Exception` base class.
    """
    return getattr(exception, 'message', next(iter(exception.args), ''))


try:
    a, = [1,2]
except (ValueError, TypeError) as exc:
    print('hello %s (%s) (%s)' % ('string', exc, get_exception_message(exc)))
