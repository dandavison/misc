a = {'categories': ['a1', 'a2']}
b = {'categories': ['b1', 'b2']}
c = {'categories': ['c1', 'c2']}
d = {'categories': ['d1', 'd2']}

xxx = [[a,b], None, [c,d]]


print set(
    category
    for xxx in xxx
    if xxx is not None
    for seq_call in xxx
    for category in seq_call['categories']
    if category not in {'b2', 'd2'}
)
