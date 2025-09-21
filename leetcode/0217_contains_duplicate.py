"""Contains duplicate.

Given an integer array nums, return true if any value appears at least
twice in the array, and return false if every element is distinct.
"""

# hashmap, O(N) time, O(N) space.


def contains_duplicate(nums: list[int]) -> bool:
    seen = set()

    for num in nums:
        if num not in seen:
            seen.add(num)
        else:
            return True

    return False


assert contains_duplicate([1, 2, 3, 1])
assert not contains_duplicate([1, 2, 3, 4])
assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
