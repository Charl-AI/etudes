"""Two sum II.

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.
"""

# two pointers, O(n) time.


def two_sum(numbers: list[int], target: int) -> list[int]:
    left = 0
    right = len(numbers) - 1

    while left < right:
        s = numbers[left] + numbers[right]
        if s == target:
            return [left + 1, right + 1]
        elif s < target:
            left += 1
        elif s > target:
            right -= 1
        else:
            raise ValueError
    raise ValueError  # no solution found


assert two_sum(numbers=[2, 7, 11, 15], target=9) == [1, 2]
assert two_sum(numbers=[2, 3, 4], target=6) == [1, 3]
assert two_sum(numbers=[-1, 0], target=-1) == [1, 2]
