def product(lists):
    if len(lists) == 0:
        return []
    elif len(lists) == 1:
        return [(el,) for el in lists[0]]
    else:
        output = []
        for l_1 in lists[0]:
            for l_2 in product(lists[1:]):
                row = [l_1]
                row.extend(l_2)
                output.append(tuple(row))
        return output


if __name__ == '__main__':
    assert product([]) == []

    assert product([[1, 2]]) == [
        (1,),
        (2,),
    ]

    assert product([[1, 2], [1, 2]]) == [
        (1, 1),
        (1, 2),
        (2, 1),
        (2, 2),
    ]

    for x in product([[1, 2, 3],
                      ['a', 'b', 'c'],
                      ['A', 'B', 'C'],
                      ['x', 'y', 'z']]):
        print(x)
