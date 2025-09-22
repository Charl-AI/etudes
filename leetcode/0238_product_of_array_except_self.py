"""Product of array except self.

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
"""

# O(n): simply compute the total product and divide by each number when iterating.
# Only trick is to deal with zeros separately since it acts as the absorbing element for the integers.


def product_except_self(nums: list[int]) -> list[int]:
    result = []
    prod = 1
    zeros = 0
    for num in nums:
        if num != 0:
            prod *= num
        else:
            zeros += 1

    if zeros > 1:
        return [0] * len(nums)

    for num in nums:
        if not zeros:
            result.append(int(prod / num))
        elif num == 0:
            result.append(prod)
        else:
            result.append(0)
    return result


assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
