"""Given an integer array nums, rotate the array to the right by k steps, where k is non-negative."""

# O(n), in-place with constant extra space using a cyclic traversal.


def rotate(nums: list[int], k: int) -> list[int]:
    n, k = len(nums), k % len(nums)
    start_idx, count = 0, 0

    while count < n:
        idx = start_idx
        prev = nums[idx]
        while True:
            next_idx = (idx + k) % n
            nums[next_idx], prev = prev, nums[next_idx]  # swap positions
            idx = next_idx
            count += 1
            if idx == start_idx:
                break

        start_idx += 1

    return nums


assert rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3) == [5, 6, 7, 1, 2, 3, 4]
assert rotate(nums=[-1, -100, 3, 99], k=2) == [3, 99, -1, -100]
