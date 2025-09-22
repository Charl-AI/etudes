"""Longest substring without repeating characters.

Given a string s, find the length of the longest substring without duplicate characters.
"""


def length_of_longest_substring(s: str) -> int:
    if len(s) <= 1:
        return len(s)

    char_to_loc = {}
    longest = 0
    left = 0

    for right, char in enumerate(s):
        if char in char_to_loc:  # char has already been seen
            left = max(left, char_to_loc[char] + 1)
        char_to_loc[char] = right
        longest = max(longest, right - left + 1)
    return longest


assert length_of_longest_substring("abcabcbb") == 3
assert length_of_longest_substring("bbbbb") == 1
assert length_of_longest_substring("pwwkew") == 3
