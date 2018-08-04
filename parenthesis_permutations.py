#!/usr/bin/env python3


def get_all_paired_paren_expressions(n):
    if n == 0:
        return {''}

    exprs = set()

    # Get all valid strings of length n-1
    sub_exprs = get_all_paired_paren_expressions(n - 1)

    for sub_expr in sub_exprs:
        # We have one new pair '(' and ')'. Find all the ways they can be inserted.

        # Find all valid insertion points for '('
        for i in range(2 * n):
            incomplete_expr = sub_expr[:i] + '(' + sub_expr[i:]

            # Find all valid insertion points for ')'
            for j in range(i + 1, 2 * n):
                complete_expr = incomplete_expr[:j] + ')' + incomplete_expr[j:]
                exprs.add(complete_expr)

    return exprs


if __name__ == '__main__':
    import sys
    n, = map(int, sys.argv[1:])

    for expr in get_all_paired_paren_expressions(n):
        print(expr)
