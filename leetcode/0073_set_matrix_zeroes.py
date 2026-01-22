"""Given an m x n matrix of integers matrix, if an element is 0, set its entire row and column to 0's.
You must update the matrix in-place."""

# O(n*m), two passes. In first pass, flag rows/cols to be zeroed. In second pass, do it.
# can optimise space by using the matrix itself to store the marker elements, but
# we don't bother with that here because it's a bit fiddly


def set_zeroes(matrix: list[list[int]]) -> list[list[int]]:
    zero_rows = [False for _ in range(len(matrix))]
    zero_cols = [False for _ in range(len(matrix[0]))]

    for row_idx, row in enumerate(matrix):
        for col_idx, element in enumerate(row):
            if element == 0:
                zero_rows[row_idx] = True
                zero_cols[col_idx] = True

    for row_idx, row in enumerate(matrix):
        for col_idx, _ in enumerate(row):
            if zero_rows[row_idx] or zero_cols[col_idx]:
                matrix[row_idx][col_idx] = 0
    return matrix


assert set_zeroes(matrix=[[0, 1], [1, 0]]) == [[0, 0], [0, 0]]

assert set_zeroes(
    matrix=[
        [1, 2, 3],
        [4, 0, 5],
        [6, 7, 8],
    ]
) == [
    [1, 0, 3],
    [0, 0, 0],
    [6, 0, 8],
]
