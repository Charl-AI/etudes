"""
The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range, then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.


This solution is O(N) time and O(N) memory. It can be trivially
changed to O(1) memory by accumulating in the loop instead of
appending to a result string. However, in Python at this scale
it basically makes no difference.
"""

MAX = 2**31 - 1
MIN = -(2**31)


def atoi(s: str) -> int:
    result = ""
    started = False
    sign = 1
    for char in s:
        if not started and char == " ":
            continue
        elif not started and char == "+":
            sign = 1
            started = True
        elif not started and char == "-":
            sign = -1
            started = True
        elif not char.isnumeric():
            break
        else:
            result += char
            started = True

    if result == "":
        return 0

    result = int(result) * sign
    result = max(result, MIN)
    result = min(result, MAX)
    return result


assert atoi("42") == 42
assert atoi(" -042") == -42
assert atoi("1337c0d3") == 1337
assert atoi("0-1") == 0
assert atoi("words and 987") == 0
print("Passed all testcases!")
