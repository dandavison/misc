class MinHeap(object):
    """
    Child nodes of item i are at 2i + 1 and 2i + 2.
    Parent node of item i is at (i - 1) / 2
    See _get_children_indexes() and _get_parent_index()
    """

    def __init__(self, values):
        self._heap = []
        for val in values:
            self.insert(val)

    def __repr__(self):
        self.print_tree()
        return ''

    def insert(self, value):
        self._heap.append(value)
        self._bubble_up(len(self._heap) - 1)

    def find_minimum(self):
        return self._heap[0]

    def pop_minimum(self):
        minimum = self._heap[0]
        last = self._heap.pop()
        if self._heap:
            self._heap[0] = last
            self._bubble_down(0)
        return minimum

    def _get_children_indexes(self, idx):
        return (2 * idx + 1,
                2 * idx + 2)

    def _get_parent_index(self, idx):
        if idx == 0:
            return None
        return (idx - 1) / 2

    def _bubble_up(self, idx):
        while True:
            parent_idx = self._get_parent_index(idx)
            if parent_idx is None:
                return
            if not self._heap[parent_idx] <= self._heap[idx]:
                self._swap_values(idx, parent_idx)
                idx = parent_idx
            else:
                return

    def _bubble_down(self, idx):
        while True:
            val = self._heap[idx]
            children = [(self._heap[_idx], _idx)
                        for _idx in self._get_children_indexes(idx)
                        if _idx < len(self._heap)]
            if not children:
                return
            min_child_val, min_child_idx = min(children)
            if not val <= min_child_val:
                self._swap_values(idx, min_child_idx)
                idx = min_child_idx
            else:
                return

    def _swap_values(self, idx1, idx2):
        self._heap[idx1], self._heap[idx2] = self._heap[idx2], self._heap[idx1]

    def print_tree(self):
        # Silly hack: create tree of directories and use `tree` utility to draw
        # tree.
        if not self._heap:
            return
        import os
        from tempfile import mkdtemp
        tempdir = mkdtemp()
        root_dir = '%s/%s' % (tempdir, self._heap[0])
        os.mkdir(root_dir)
        self._make_directory_tree(0, root_dir)
        os.chdir(tempdir)
        _ = os.system('tree --noreport')
        os.system('rm -r %s' % tempdir)

    def _make_directory_tree(self, root_idx, root_dir):
        import os
        for child_idx in self._get_children_indexes(root_idx):
            if child_idx >= len(self._heap):
                continue
            child_dir = '%s/%s' % (root_dir, self._heap[child_idx])
            os.mkdir(child_dir)
            self._make_directory_tree(child_idx, child_dir)


if __name__ == '__main__':
    h = MinHeap([])
    for i in [3, 1, 5, 2, 4, 0.5]:
        print('insert %d' % i)
        h.insert(i)
        print(h._heap)
