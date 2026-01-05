"""Given a roman numeral, convert it to an integer."""

# O(n), first split into valid chunks (similar to lexing),
# then map each chunk to its value and sum (similar to parsing)

ROMANS = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

SPECIALS = {
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900,
}

ALL_TOKENS = ROMANS | SPECIALS


def chunk(s: str) -> list[str]:
    chunks, i = [], 0
    while i < len(s):
        two_chars = s[i : i + 2]  # slicing handles EOS gracefully
        if two_chars in SPECIALS:
            chunks.append(two_chars)
            i += 2  # skip next char if it belongs to this special token
        else:
            chunks.append(s[i])
            i += 1
    return chunks


def roman_to_int(s: str) -> int:
    return sum(map(lambda c: ALL_TOKENS[c], chunk(s)))


assert roman_to_int("III") == 3
assert roman_to_int("XLIX") == 49
