from collections import Iterable
from collections import Mapping
from collections import Sequence
import json


def serializable(obj):
    """
    Convert obj to serializable data structures.

    Mapping -> dict
    Sequence -> list
    non-Sequence Iterable -> sorted list
    """
    if isinstance(obj, basestring):
        return obj
    elif isinstance(obj, Mapping):
        # E.g. frozenset() is a valid key that is not json-serializable.
        return {serializable(key): serializable(value)
                for key, value in obj.iteritems()}
    elif isinstance(obj, Sequence):
        return map(serializable, obj)
    elif isinstance(obj, Iterable):
        return sorted(map(serializable, obj))
    else:
        try:
            json.dumps(obj)
            return obj
        except TypeError:
            return unicode(obj)
