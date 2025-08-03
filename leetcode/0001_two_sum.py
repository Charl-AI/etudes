def two_sum(nums: list[int], target: int) -> list[int]:
    num_to_idx = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in num_to_idx:
            return [num_to_idx[diff], i]
        num_to_idx[n] = i

    raise ValueError("Could not find a valid pair")


assert two_sum([2, 7, 11, 15], 9) == [0, 1]
assert two_sum([3, 2, 4], 6) == [1, 2]
assert two_sum([3, 3], 6) == [0, 1]
print("Passed all testcases!")
