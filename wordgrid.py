board = [
   ['A','B','C','E'],
   ['S','F','C','S'],
   ['A','D','E','E'],
]
# //
# // word = "ABCCED", -> returns true,
# // word = "SEE", -> returns true,
# // word = "ABCB", -> returns false.
# // word = "ABCESCFSADEE", -> returns true.


def exists(word, board):
    for cell in _get_cells(word[0], board):        
        # print('Trying starting cell: %s' % (cell,))
        seen = set()
        if _exists(word[1:], cell, board, seen):
            return True    
    return False


def _exists(word, cell, board, seen):
    if not word:
        return True
    for next_cell in _get_neighbors(cell, board):        
        # print('Trying next cell %s' % (next_cell,))
        if next_cell in seen:
            continue
        else:
            seen.add(next_cell)
        i, j = next_cell
        if board[i][j] == word[0]:
            result = _exists(word[1:], next_cell, board, seen)
            if result:
                return True
    return False


def _get_neighbors(cell, board):
    n_rows = len(board)
    n_cols = len(board[0])
    i, j = cell
    verticals = []
    horizontals = []
    if i > 0:
        verticals.append(i - 1)
    if i < n_rows - 1:
        verticals.append(i + 1)
    if j > 0:
        horizontals.append(j - 1)
    if j < n_cols - 1:
        horizontals.append(j + 1)

    for new_i in verticals:
        yield new_i, j
    for new_j in horizontals:
        yield i, new_j
        
            
def _get_cells(char, board):
    n_rows = len(board)
    n_cols = len(board[0])
    for i in range(n_rows):
        for j in range(n_cols):
            if board[i][j] == char:
                yield i, j
                
                

print(exists('AX', board), False)
print(exists("ABCCED", board), True)
print(exists("SEE", board), True)
print(exists("ABCB", board), False)
print(exists("ABCESCFSADEE", board), True)
