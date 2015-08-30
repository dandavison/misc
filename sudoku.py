import numpy as np


class Sudoku(object):
    def __init__(self, cells):
        # self.cells = np.array([["%d,%d" % (j, i) for i in range(9)] for j in range(9)])
        self.cells = np.array([[set(range(9)) for i in range(9)]
                               for j in range(9)])
        for index, value in cells.items():
            self.cells[index] = {value}
        
    def get_block(self, i, j):
        rows = [k for k in range(9) if k / 3 == i]
        columns = [k for k in range(9) if k / 3 == j]
        row_slice = slice(min(rows), max(rows) + 1)
        column_slice = slice(min(columns), max(columns) + 1)
        return self.cells[row_slice, column_slice]

    def check(self):
        
        
        for i in range(3):
            self.eliminate(self.cells[i, :])

        for j in range(3):
            self.eliminate(self.cells[:, j])

        for i in range(3):
            for j in range(3):
                self.eliminate(self.get_block(i, j).ravel())
        
    def solve(self):

        it = 0
        
        while True:
            for i in range(3):
                self.eliminate(self.cells[i, :])
    
            for j in range(3):
                self.eliminate(self.cells[:, j])
    
            for i in range(3):
                for j in range(3):
                    self.eliminate(self.get_block(i, j).ravel())

            if all(len(values) == 1 for values in self.cells.ravel()):
                print 'solved!'
                return self

            it += 1

            if it == 100:
                return self
            
            
    def eliminate(self, cells):
        
        # Find all determined values
        determined = set()
        for values in cells:
            if len(values) == 1:
                [value] = values
                try:
                    assert value not in determined
                except:
                    print 'Expected value (%s) to not be in determined (%s)' % (
                        value,
                        sorted(determined))
                    print self
                    raise
                determined.update(values)

        # Remove them from the other cells
        for values in cells:
            if len(values) > 1:
                if determined & values:
                    print "Eliminating %s from cell containing %s" % (
                        str(sorted(determined & values)),
                        sorted(values))
                    values -= determined
                    if len(values) == 1:
                        print "Determined a value!"
                
                    
    def __repr__(self):
        chars = ''
        for i in range(9):
            for j in range(9):
                if len(self.cells[i, j]) == 1:
                    [value] = self.cells[i, j]
                    chars += str(value)
                else:
                    chars += '.'
                chars += ' '
            chars += '\n'
        return chars
    


if True or __name__ == '__main__':
    cells = {
        (0, 1): 9,
        (0, 2): 1,
        (0, 7): 6,
    
        (1, 0): 8,
        (1, 5): 9,
        (1, 6): 1,
        (1, 8): 4,
    
        (2, 1): 5,
        (2, 4): 1,
        (2, 5): 8,
        (2, 8): 3,
    
        (3, 1): 7,
        (3, 2): 6,
    
        (4, 2): 8,
        (4, 6): 2,
    
        (5, 6): 6,
        (5, 7): 7,
    
        (6, 0): 1,
        (6, 3): 9,
        (6, 4): 3,
        (6, 7): 4,
    
        (7, 0): 3,
        (7, 2): 5,
        (7, 3): 4,
        (7, 8): 7,
    
        (8, 1): 2,
        (8, 6): 3,
        (8, 7): 8,
        
    }
    sudoku = Sudoku(cells)
    print sudoku
    print sudoku.solve()        
