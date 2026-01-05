"""Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet."""

import string

# O(log n) iteration style


def convert_to_title(col_number: int) -> str:
    res = ""
    while col_number > 0:
        col_number -= 1
        res += string.ascii_uppercase[col_number % 26]
        col_number //= 26
    return res[::-1]  # reverse to get final result


assert convert_to_title(32) == "AF"
