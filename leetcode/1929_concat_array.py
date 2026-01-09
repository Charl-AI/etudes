"""Given an integer array nums of length n, you want to create an array ans of length 2n where
ans is the concatenation of two nums arrays."""

# O(n). Avoiding inbuilt concatenation (nums + nums) for practice


def concat_array(nums: list[int]) -> list[int]:
    n = len(nums)
    res: list[int] = [0 for _ in range(n * 2)]
    for i in range(n):
        res[i] = nums[i]
        res[i + n] = nums[i]
    return res


assert concat_array(nums=[1, 4, 1, 2]) == [1, 4, 1, 2, 1, 4, 1, 2]
