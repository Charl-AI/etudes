"""Longest consecutive sequence.

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
"""

# O(n) time, O(n) space. Trick is to convert to set, then use the fact
# that sequences can only start on values where num-1 is not in the set.


def longest_consecutive(nums: list[int]) -> int:
    unique = set(nums)
    best = 0
    for num in nums:
        if num - 1 not in unique:
            i = 1
            while num + i in unique:
                i += 1
            best = max(best, i)
    return best


assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
assert longest_consecutive([1, 0, 1, 2]) == 3
