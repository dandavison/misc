#!/usr/bin/env python3

def map_dict(in_dict, rules):

    out_dict = {}

    for in_path, out_path in rules.items():
        val = get(in_path, in_dict)
        update(out_dict, out_path, val)

    return out_dict


def get(path, cursor):
    path = path.split('.')
    for key in path:
        cursor = cursor[key]
    return cursor


def update(_dict, path, val):
    path = path.split('.')
    *path, terminal_key = path
    for key in path:
        if key not in _dict:
            _dict[key] = {}
        _dict = _dict[key]
    _dict[terminal_key] = val


if __name__ == '__main__':

    def assert_equal(a, b):
        if a != b:
            print(a)
            print(b)
            exit(1)

    # 1 -----------------------------------------------------------------------
    data = {
        'a': 'a-val',
    }
    rules = {
        'a': 'A',
    }
    assert_equal(
        map_dict(data, rules),
        {'A': 'a-val'},
    )
    # -------------------------------------------------------------------------


    # 2 -----------------------------------------------------------------------
    data = {
        'a': {
            'b': 'b-val',
        }
    }
    rules = {
        'a.b': 'B',
    }
    assert_equal(
        map_dict(data, rules),
        {'B': 'b-val'},
    )
    # -------------------------------------------------------------------------


    # 3 -----------------------------------------------------------------------
    data = {
        'a': {
            'b': {
                'c': 'c-val',
            }
        }
    }
    rules = {
        'a.b.c': 'C',
    }
    assert_equal(
        map_dict(data, rules),
        {'C': 'c-val'},
    )
    # -------------------------------------------------------------------------


    # 4 -----------------------------------------------------------------------
    data = {
        'a': {
            'b': {
                'c': 'c-val',
            }
        }
    }
    rules = {
        'a.b.c': 'A.B.C',
    }
    assert_equal(
        map_dict(data, rules),
        {
            'A': {
                'B': {
                    'C': 'c-val',
                }
            }
        }
    )
    # -------------------------------------------------------------------------
