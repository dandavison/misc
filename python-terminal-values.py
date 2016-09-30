#!/usr/bin/env python3

def get_terminal_values_1(d):
    message = {}
    for key, val in d.items():
        if isinstance(val, dict):
            for k, v in val.items():
                new_key = "{outer_key}__{inner_key}".format(outer_key=key, inner_key=k)
                message[new_key] = v
        else:
            message[key] = val
    return message


def _get_terminal_values(d, path):
    for key, val in d.items():
        _path = key if path is None else '%s__%s' % (path, key)
        if isinstance(val, dict):
            yield from _get_terminal_values(val, _path)
        else:
            yield _path, val

def get_terminal_values_2(d):
    return dict(_get_terminal_values(d, None))


d1 = {
    'k1': {'k2': 2},
    'k3': 3,
}


print(get_terminal_values_1(d1))

print(get_terminal_values_2(d1))

d2 = {
    'k1': {'k2': 2},
    'k3': 3,
    'k4': {'k5': {'k6': 6}, 'k7': 7}
}


print(get_terminal_values_2(d2))
