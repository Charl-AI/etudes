"""Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array.
The result should also be sorted in ascending order.
"""


# O(k + log n) - binary search to find target / insertion point,
# then build the window by expanding two pointers from the target idx.


def find_target(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    while left < right:
        idx = left + (right - left) // 2
        if arr[idx] <= target:
            left = idx + 1
        elif arr[idx] > target:
            right = idx
        else:
            raise ValueError
    return left


def find_k_closest(arr: list[int], k: int, x: int) -> list[int]:
    target_idx = find_target(arr, x)

    left, right = target_idx, target_idx
    while right - left < k:
        if right >= len(arr):
            left -= 1
        elif left <= 0:
            right += 1
        elif abs(arr[right] - x) < abs(arr[left - 1] - x):
            right += 1
        else:
            left -= 1
    res = arr[left:right]
    return res


assert find_k_closest(arr=[2, 4, 5, 8], k=2, x=6) == [4, 5]
assert find_k_closest(arr=[1, 2, 3, 4, 5], k=4, x=3) == [1, 2, 3, 4]
assert find_k_closest(arr=[1, 1, 2, 3, 4, 5], k=4, x=-1) == [1, 1, 2, 3]
assert find_k_closest(arr=[2, 3, 4], k=3, x=1) == [2, 3, 4]
assert find_k_closest(arr=[1, 2, 3, 4, 5], k=4, x=10) == [2, 3, 4, 5]
assert find_k_closest(arr=[10, 20, 30, 40, 50], k=2, x=25) == [20, 30]
