"""Group anagrams.

Given an array of strings strs, group the anagrams together.
You can return the answer in any order.
"""

from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    result = defaultdict(list)

    for s in strs:
        fingerprint = defaultdict(int)
        for char in s:
            fingerprint[char] += 1
        result[frozenset(fingerprint.items())].append(s)
    return list(result.values())


assert group_anagrams([""]) == [[""]]
assert group_anagrams(["a"]) == [["a"]]
assert group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"],
]
