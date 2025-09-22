"""Valid palindrome.

A phrase is a palindrome if, after converting all uppercase letters into lowercase
letters and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.
"""


# two pointers, O(n) time

import string

VALID = string.ascii_lowercase + string.digits


def valid_palindrome(s: str) -> bool:
    s_arr = [char for char in s.lower() if char in VALID]
    if len(s_arr) <= 1:
        return True

    left = 0
    right = len(s_arr) - 1
    while left < right:
        if s_arr[left] != s_arr[right]:
            return False
        left += 1
        right -= 1
    return True


assert valid_palindrome(" ")
assert not valid_palindrome("race a car")
assert valid_palindrome("A man, a plan, a canal: Panama")
