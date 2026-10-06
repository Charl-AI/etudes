# O(log n): process one digit at a time
# the range of inputs is small enough that we can build a lookup table manually for each
# digit, but you could in principle build it with code too (probably more fiddly -> not worth it).

# fmt: off
DIGITS = {
    0: "",
    1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX",
    10: "X", 20: "XX", 30: "XXX", 40: "XL", 50: "L", 60: "LX", 70: "LXX", 80: "LXXX", 90: "XC",
    100: "C", 200: "CC", 300: "CCC", 400: "CD", 500: "D", 600: "DC", 700: "DCC", 800: "DCCC", 900: "CM",
    1000: "M", 2000: "MM", 3000: "MMM",
}
# fmt: on


def int_to_roman(num: int) -> str:
    out = ""
    mult = 1
    while num:
        num, rem = divmod(num, 10)
        out = DIGITS[rem * mult] + out
        mult *= 10
    return out


assert int_to_roman(3) == "III"
assert int_to_roman(10) == "X"
assert int_to_roman(49) == "XLIX"
assert int_to_roman(58) == "LVIII"
assert int_to_roman(1994) == "MCMXCIV"
assert int_to_roman(3749) == "MMMDCCXLIX"
