"""Given a 2D integer array matrix, return the transpose of matrix."""

# pretty straightforward, simply O(nm) in time and extra
# space, where n,m are rows and cols. In a real matrix lib, you would
# probably not actually transpose it in memory and simply
# return a 'view' by flipping the indices in the getitem method


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    rows, cols = len(matrix), len(matrix[0])
    out = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            out[j][i] = matrix[i][j]
    return out


assert transpose([[2, 1], [-1, 3]]) == [[2, -1], [1, 3]]
