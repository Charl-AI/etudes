"""You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.
"""

# O(n*m), reverse rows, then transpose trick.


def rotate(matrix: list[list[int]]):
    matrix.reverse()  # reverse rows

    for row_idx, row in enumerate(matrix):
        for col_idx, _ in enumerate(row):
            if col_idx <= row_idx:
                continue
            tmp = matrix[row_idx][col_idx]
            matrix[row_idx][col_idx] = matrix[col_idx][row_idx]
            matrix[col_idx][row_idx] = tmp
    return matrix


assert rotate(matrix=[[1, 2], [3, 4]]) == [[3, 1], [4, 2]]
assert rotate(
    matrix=[
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
) == [
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3],
]
