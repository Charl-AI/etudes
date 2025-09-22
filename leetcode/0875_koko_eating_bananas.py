"""Koko eating bananas.

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.
"""

# we will reframe this as a binary search problem, which is O(log m) time,
# where m is the maximum possible speed (i.e. the maximum bananas per pile).
# since we also do an O(n) operation (evaluating time_taken) in the inner
# loop, it comes out to O(nlogm), where n is the number of piles.

# (of course, evaluating time_taken is embarassingly parallelisable, so
# in practice, it should be easy to get it down to O(log m)).

import math


def min_eating_speed(piles: list[int], h: int):
    upper = max(piles)
    lower = 1
    best = upper

    def time_taken(speed: int) -> int:
        return sum(map(lambda x: math.ceil(x / speed), piles))

    while lower < upper:
        mid = lower + (upper - lower) // 2
        if time_taken(mid) <= h:
            upper = mid
            best = upper
        else:
            lower = mid + 1
    return best


assert min_eating_speed(piles=[3, 6, 7, 11], h=8) == 4
assert min_eating_speed(piles=[30, 11, 23, 4, 20], h=5) == 30
assert min_eating_speed(piles=[30, 11, 23, 4, 20], h=6) == 23
