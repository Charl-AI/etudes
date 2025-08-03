"""String t is a divisor of string s iff there exists
a k for which t * k == s, where * is the string repeat
operation (i.e. 'a' * 2 = 'aa').

Given two strings, return their greatest common divisor.

Approach:
- start with gcd := the smaller of the two
- check if gcd is a divisor of both strings
- return gcd if true, else pop the last element and repeat

O(n) time complexity, where n is min(len(str1),len(str2)).
"""


def is_divisor(t: str, s: str) -> bool:
    """True if t is a divisor of s."""

    return t * (len(s) // len(t)) == s


def string_gcd(str1: str, str2: str) -> str:
    l1 = len(str1)
    l2 = len(str2)
    if l1 < l2:
        gcd = str1
    else:
        gcd = str2

    for _ in reversed(gcd):
        if is_divisor(gcd, str1) and is_divisor(gcd, str2):
            return gcd

        gcd = gcd[:-1]  # pop last char

    return gcd


assert string_gcd("ABCABC", "ABC") == "ABC"
assert string_gcd("ABABAB", "ABAB") == "AB"
assert string_gcd("LEET", "CODE") == ""
print("Passed all testcases!")
