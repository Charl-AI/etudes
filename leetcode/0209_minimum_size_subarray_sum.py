# sliding window, O(n). Expand window by moving rhs pointer
# until the target is reached or exceded, then contract window


def min_subarray_len(target: int, nums: list[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return int(nums[0] >= target)

    res = float("inf")
    lhs = 0
    subsum = 0  # sum of current subarray

    for rhs, num in enumerate(nums):
        subsum += num
        while subsum >= target:
            res = int(min(rhs - lhs + 1, res))
            subsum -= nums[lhs]
            lhs += 1

    return res if isinstance(res, int) else 0  # 0 iff res never updated from 'inf'


assert min_subarray_len(target=5, nums=[1, 2, 1]) == 0
assert min_subarray_len(target=10, nums=[2, 1, 5, 1, 5, 3]) == 3
assert min_subarray_len(target=7, nums=[2, 3, 1, 2, 4, 3]) == 2
