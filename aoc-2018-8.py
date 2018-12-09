def parse_tree(stream):
    n_child, n_meta = next(stream), next(stream)
    children = [parse_tree(stream) for _ in range(n_child)]
    return {
        'metadata': [next(stream) for _ in range(n_meta)],
        'children': children ,
    }


def sum_metadata(node):
    total = sum(node['metadata'])
    for child in node['children']:
        total += sum_metadata(child)
    return total


def get_value(node):
    children = node['children']
    if not children:
        return sum(node['metadata'])
    else:
        return sum(get_value(children[i - 1]) for i in node['metadata'] if 0 < i <= len(children))


import sys
stream = map(int, sys.stdin.read().strip().split())
tree = parse_tree(stream)
# part 1
print(sum_metadata(tree))
# part 2
print(get_value(tree))
