from __future__ import print_function

import ast
import sys


def find_atypical_super_calls(tree):
    class_defs = [node for node in ast.walk(tree) if type(node) == ast.ClassDef]
    for class_def in class_defs:
        for node in ast.walk(class_def):
            if type(node) == ast.Call:
                call = node
                func = call.func
                if not hasattr(func, 'id'):
                    continue
                if func.id == 'super':
                    if type(call.args[0]) == ast.Name:
                        if call.args[0].id != class_def.name:
                            yield call.lineno, call.col_offset, f'{class_def.name} {call.args[0].id}'
                    else:
                        yield call.lineno, call.col_offset, f'??????????????'


if __name__ == '__main__':
    path, = sys.argv[1:]
    with open(path) as fp:
        tree = ast.parse(fp.read())
    for lineno, col_offset, text in find_atypical_super_calls(tree):
        print(f'{path}:{lineno}:{col_offset}: {text}')
