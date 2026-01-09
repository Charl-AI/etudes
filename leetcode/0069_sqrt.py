"""Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.
"""

# binary search O(log n)
# can also use newton-raphson for O(log n) but faster practical convergence


def sqrt(x: int) -> int:
    lhs, rhs = 1, x
    res = 0

    while lhs <= rhs:
        candidate = lhs + (rhs - lhs) // 2
        sq = candidate * candidate

        if sq > x:
            rhs = candidate - 1
        elif sq < x:
            lhs = candidate + 1
            res = candidate  # stores the best result less than target
        else:
            return candidate  # returns if exact sqrt
    return res  # returns rounded down result if not exact


assert sqrt(4) == 2
assert sqrt(8) == 2  # rounded to nearest int
assert sqrt(9) == 3
