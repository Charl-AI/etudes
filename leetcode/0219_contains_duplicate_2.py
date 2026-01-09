"""Given an integer array nums and an integer k,
return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""

from collections import defaultdict

# O(n) time, O(k) space using a hashset / defaultdict and a sliding window.


def contains_duplicate(nums: list[int], k: int) -> bool:
    if len(nums) <= 1:
        return False

    i, j = 0, k
    window = defaultdict(int)

    # build initial window
    for t in range(i, j + 1):
        window[nums[t]] += 1
        if window[nums[t]] > 1:
            return True  # duplicate in initial window

    while j < len(nums) - 1:
        window[nums[i]] -= 1  # goes out of window
        i += 1
        j += 1
        window[nums[j]] += 1
        if window[nums[j]] > 1:
            return True

    return False


assert contains_duplicate(nums=[1, 2, 3, 1], k=3)
assert not contains_duplicate(nums=[1, 2, 3, 1, 2, 3], k=2)
