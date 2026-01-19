"""Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise."""

# O(n) sliding window with frequency table to check for anagrams of s1

import string


# important: we would usually use defaultdict, but there is a trap where:
# {"a": 0, "b": 1} != {"b": 1} (i.e. keys with 0 values mess up equality checks)
# we workaround this by making our own dict with all necessary keys initialised
def _build_fp_table():
    return {c: 0 for c in string.ascii_lowercase}


def check_inclusion(s1: str, s2: str) -> bool:
    if len(s2) < len(s1):
        return False

    s1_fp, s2_fp = _build_fp_table(), _build_fp_table()  # fingerprint table
    for char1, char2 in zip(s1, s2):
        s1_fp[char1] += 1
        s2_fp[char2] += 1

    left, right = 0, len(s1) - 1
    while right < len(s2) - 1:
        if s1_fp == s2_fp:
            return True
        right += 1
        s2_fp[s2[right]] += 1
        s2_fp[s2[left]] -= 1
        left += 1

    return s1_fp == s2_fp  # check final window


assert check_inclusion(s1="adc", s2="dcda")
assert check_inclusion(s1="ab", s2="eidbaooo")
assert check_inclusion(s1="abc", s2="lecabee")
assert not check_inclusion(s1="ab", s2="eidboaoo")
assert not check_inclusion(s1="abc", s2="lecaabee")
