"""Search in rotated sorted array.

There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly left rotated at an unknown
index k (1 <= k < nums.length) such that the resulting array is
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.
"""

# binary search, O(log n) time. The trick is to do two (or three) binary searches:
# one to find the cut/pivot point. And then one in the relevant partition(s).


def search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    # first, find point where the array was partitioned
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    pivot = left

    def inner(left, right):  # classic binary search
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    result = inner(0, pivot - 1)
    if result != -1:
        return result
    else:
        return inner(pivot, len(nums) - 1)


assert search(nums=[4, 5, 6, 7, 0, 1, 2], target=0) == 4
assert search(nums=[4, 5, 6, 7, 0, 1, 2], target=3) == -1
assert search(nums=[1], target=0) == -1
assert search(nums=[1], target=1) == 0
