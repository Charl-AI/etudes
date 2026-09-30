def diagonal_sum(mat: list[list[int]]) -> int:
    res = 0
    N = len(mat)

    # 'forward' diagonal
    for i in range(N):
        res += mat[i][i]

    # 'reverse' diagonal
    for i in range(N):
        res += mat[i][N - 1 - i]

    if N % 2 != 0:
        res -= mat[N // 2][N // 2]

    return res


assert diagonal_sum(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 25
assert diagonal_sum(mat=[[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]) == 8
assert diagonal_sum(mat=[[5]]) == 5
