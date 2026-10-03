# NB: problem assumes 32 bit input, thus we only have to go up to the billions
# Approach: write a function that solves the problem for 3-digit numbers 'i.e. one hundred thirty one'
# then simply chunk the number into groups of three and add the suffix 'thousand', 'million', or 'billion'
# onto the relevant chunks. Constant time per chunk, so log n time overall


# fmt: off
DIGITS = {
    1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
    6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
    11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen",
    16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen",
}

TENS = {2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty",
      6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety",
}
# fmt: on


def n2w_three_digit(s: str) -> str:
    # takes a string left-padded to three digits: e.g. 12 is '012'
    assert len(s) == 3
    out = ""

    if s[0] != "0":
        out += f"{DIGITS[int(s[0])]} Hundred "

    if s[1] == "0":
        if s[2] == "0":
            return out.strip()
        out += DIGITS[int(s[2])]
        return out

    if s[1] == "1":
        out += DIGITS[int(s[1:])]
        return out

    out += TENS[int(s[1])]
    if s[2] != "0":
        out += f" {DIGITS[int(s[2])]}"
    return out


def lpad_stringify(num: int) -> str:
    # convert num [0,100) to left padded string
    out = str(num)
    pad = "0" * (3 - len(out))
    return f"{pad}{out}"


def number_to_words(num: int) -> str:
    if not num:
        return "Zero"
    res = ""
    SUFFIX = {0: "", 1: " Thousand", 2: " Million", 3: " Billion"}
    suff = 0
    while num:
        num, x = num // 1000, num % 1000
        x = lpad_stringify(x)
        prefix = n2w_three_digit(x)
        suffix = SUFFIX[suff] if prefix else ""
        space = " " if prefix else ""
        res = f"{prefix}{suffix}{space}{res}"
        suff += 1
    return res.strip()


assert number_to_words(0) == "Zero"
assert number_to_words(100) == "One Hundred"
assert number_to_words(1000000) == "One Million"
assert number_to_words(1000010) == "One Million Ten"
assert number_to_words(123) == "One Hundred Twenty Three"
assert number_to_words(12345) == "Twelve Thousand Three Hundred Forty Five"
assert (
    number_to_words(1234567)
    == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
)
