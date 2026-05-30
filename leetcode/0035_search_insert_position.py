"""Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order."""

# O(logn) binary search


def search_insert(nums: list[int], target: int) -> int:
    lhs, rhs = 0, len(nums)

    while lhs < rhs:
        mid = lhs + (rhs - lhs) // 2
        val = nums[mid]

        if val == target:
            return mid
        elif val > target:
            rhs = mid
        elif val < target:
            lhs = mid + 1
    return lhs


assert search_insert(nums=[-1, 0, 2, 4, 6, 8], target=5) == 4
assert search_insert(nums=[-1, 0, 2, 4, 6, 8], target=10) == 6
