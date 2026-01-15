"""Design an algorithm to encode a list of strings to a string.
The encoded string is then sent over the network and is decoded back to the original list of strings.
"""

# O(n) encoding, where n is number of strings.
# O(nm) decoding, nm is total number of chars.
# encode strings with a prefix representing their length + a delimiter

DELIMITER = "#"


def encode(strs: list[str]) -> str:
    out = ""
    for s in strs:
        out += f"{len(s)}" + DELIMITER + s
    return out


def decode(s: str) -> list[str]:
    res, i, j = [], 0, 0
    while i < len(s):
        while s[j] != DELIMITER:
            j += 1  # find next '#'
        length = int(s[i:j])  # get length of str
        i = j + 1
        j = i + length
        res.append(s[i:j])  # extract str
        i = j  # move on to next str
    return res


TEST_CASES = [
    [""],
    ["Hello", "World"],
    ["Example sentence", "another sentence"],
]

for test_case in TEST_CASES:
    assert decode(encode(test_case)) == test_case
