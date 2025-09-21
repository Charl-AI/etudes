"""Valid anagram.

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""

# option 1: O(nlogn), sort and check for equality
# option 2: O(n), frequency map

from collections import defaultdict


def valid_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    seen_s = defaultdict(int)
    seen_t = defaultdict(int)

    for s_char, t_char in zip(s, t):
        seen_s[s_char] += 1
        seen_t[t_char] += 1

    return seen_s == seen_t


assert valid_anagram("anagram", "nagaram")
assert not valid_anagram("rat", "car")
