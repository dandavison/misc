def selectionsort(array):
    # Find 1st smallest; swap with array first
    # Find 2nd smallest; swap with array second
    # ...

    def find_min_and_swap(offset):
        _min = float('inf')
        _min_index = None
        for i in range(offset, len(array)):
            if array[i] < _min:
                _min = array[i]
                _min_index = i
        array[offset], array[_min_index] = _min, array[offset]

    for i in range(len(array))[:5]:
        find_min_and_swap(i)

    return array


def quicksort(array):
    if len(array) == 2:
        if array[0] <= array[1]:
            return array
        else:
            return [array[1], array[0]]
    else:
        halfway = len(array) // 2




if __name__ == '__main__':
    sorters = [
        selectionsort,
    ]
    data = [
        [],
        [1],
        [2, 1],
        [6, 3 ,4, 1, 2, 5],
    ]
    for sorter in sorters:
        for array in data:
            assert(sorter(array) == sorted(array))
