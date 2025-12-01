"""Given an integer array nums of unique elements, return all possible subsets (the power set)."""

# O n2^n


def subsets(nums: list[int]) -> list[list[int]]:
    res = [[]]

    for num in nums:
        res += [subset + [num] for subset in res]
    return res


assert subsets(nums=[1, 2, 3]) == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
