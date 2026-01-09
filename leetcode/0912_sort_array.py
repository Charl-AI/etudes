"""Given an array of integers nums, sort the array in ascending order and return it."""

# quicksort, classic O(nlogn) time, O(nlogn) space, easy to implement


def quick_sort(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums

    pivot = nums[len(nums) // 2]

    left = [x for x in nums if x < pivot]
    mid = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)


assert quick_sort(nums=[5, 2, 3, 1]) == [1, 2, 3, 5]
assert quick_sort(nums=[5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5]


# merge sort, O(nlogn) time, O(n) space


def merge(left, right):
    res, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res


def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums

    pivot_idx = len(nums) // 2
    left = merge_sort(nums[:pivot_idx])
    right = merge_sort(nums[pivot_idx:])
    return merge(left, right)


assert merge_sort(nums=[5, 2, 3, 1]) == [1, 2, 3, 5]
assert merge_sort(nums=[5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5]
