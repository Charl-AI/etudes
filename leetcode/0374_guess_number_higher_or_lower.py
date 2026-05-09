def guess(guess):
    num = ...  # true number
    if num < guess:
        return -1
    if num > guess:
        return 1
    return 0


# simple binary search O(log n)


def guess_number(n: int) -> int:
    lhs, rhs = 1, n

    while lhs < rhs:
        mid = lhs + (rhs - lhs) // 2
        res = guess(mid)
        if res == -1:
            rhs = mid
        elif res == 1:
            lhs = mid + 1
        else:
            return mid

    return lhs
