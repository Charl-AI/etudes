"""Plus one.
You are given a large integer represented as an integer array digits,
where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

# No tricks here, just O(n) time and space.


def plus_one(digits: list[int]) -> list[int]:
    result = []
    carry = 1
    for digit in reversed(digits):
        if carry and digit != 9:
            result.append(digit + carry)
            carry = 0
        elif carry:
            result.append(0)
            carry = 1
        else:
            result.append(digit)

    if carry:  # deals with the [9,9,9] case etc.
        result.append(1)
    return list(reversed(result))


assert plus_one([1, 2, 3]) == [1, 2, 4]
assert plus_one([4, 3, 2, 1]) == [4, 3, 2, 2]
assert plus_one([9]) == [1, 0]
