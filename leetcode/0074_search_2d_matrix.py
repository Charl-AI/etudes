"""Search a 2D matrix.

You are given an m x n integer matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""

# we can get O(log mn) pretty easily by just treating the matrix as one long list
# and doing binary search. Collapsing the matrix is easy, since it's already sorted
# we just need to figure out a 'view' that maps a 1D index to the 2D indices.

# let's use the convention of a mxn matrix having m rows and n cols.
# I.e. we can think of the matrix as stacked row vectors


def flat_to_2d(idx: int, n: int):
    return idx // n, idx % n


def search_matrix(matrix: list[list[int]], target: int) -> bool:
    m = len(matrix)
    n = len(matrix[0])

    min = 0
    max = m * n

    while min < max:
        idx = min + (max - min) // 2
        y, x = flat_to_2d(idx, n)
        val = matrix[y][x]
        if val == target:
            return True
        elif val < target:
            min = idx + 1
        elif val > target:
            max = idx
        else:
            raise ValueError
    return False


assert search_matrix(
    matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3
)
assert not search_matrix(
    matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13
)
