"""Determine if a 9 x 9 Sudoku board is valid."""

# simple O(rows*cols) hashing. Only tricky part is the index math
# to figure out which sub-box each element belongs to.


def _get_box_idx(row_idx, col_idx) -> int:
    return (row_idx // 3) * 3 + (col_idx // 3)


def valid_sudoku(board: list[list[str]]) -> bool:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxs = [set() for _ in range(9)]

    for row_idx, row in enumerate(board):
        for col_idx, element in enumerate(row):
            if element == ".":
                continue
            el = int(element)
            box_idx = _get_box_idx(row_idx, col_idx)
            if el in rows[row_idx] or el in cols[col_idx] or el in boxs[box_idx]:
                return False
            else:
                rows[row_idx].add(el)
                cols[col_idx].add(el)
                boxs[box_idx].add(el)
    return True


assert valid_sudoku(
    board=[
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
)

assert not valid_sudoku(
    board=[
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
)
