"""The Tribonacci sequence Tn is defined as follows:
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.
"""

# O(n) using caching to avoid recomputation

import functools


@functools.cache
def trib(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return trib(n - 1) + trib(n - 2) + trib(n - 3)


assert trib(3) == 2
assert trib(21) == 121415
