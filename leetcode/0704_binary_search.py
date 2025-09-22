"""Binary search.

Given an array of integers nums which is sorted in ascending order,
and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.
"""

# binary search is O(log n). It's worth putting in the time to write
# this function fast. Note python has it built in in the bisect module


def binary_search(nums: list[int], target: int) -> int:
    if len(nums) == 0:
        return -1

    min = 0
    max = len(nums)
    while min < max:
        idx = min + (max - min) // 2
        if nums[idx] == target:
            return idx
        elif nums[idx] < target:
            min = idx + 1
        elif nums[idx] > target:
            max = idx
    return -1


assert binary_search(nums=[-1, 0, 3, 5, 9, 12], target=9) == 4
assert binary_search(nums=[-1, 0, 3, 5, 9, 12], target=2) == -1
