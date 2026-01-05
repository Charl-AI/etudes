"""You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

import functools

# classic dynamic programming problem, O(n).
# From the top of the staircase, there's 1 way to
# get to the top. For each other step, we can choose
# to climb 1 or 2 at a time, so we add together both
# possibilities, caching as we go.


def climb_stairs(n: int) -> int:
    @functools.cache
    def inner(x):
        if x == n:
            return 1
        if x > n:
            return 0
        return inner(x + 1) + inner(x + 2)

    return inner(0)


assert climb_stairs(2) == 2
assert climb_stairs(3) == 3
