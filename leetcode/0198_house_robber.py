"""You are planning to rob money from the houses with values represented by the given array.
But you cannot rob two adjacent houses because the security system
will automatically alert the police if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police."""

# O(n) dynamic programming

import functools


def rob(nums: list[int]) -> int:
    @functools.cache
    def inner(idx):
        if idx >= len(nums):
            return 0

        return max(
            nums[idx] + inner(idx + 2),  # rob the house, skipping next one
            inner(idx + 1),  # do nothing, and have the option to rob next one
        )

    return inner(0)


assert rob(nums=[1, 1, 3, 3]) == 4
assert rob(nums=[2, 9, 8, 3, 6]) == 16
