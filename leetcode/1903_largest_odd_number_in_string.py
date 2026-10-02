def largest_odd_number(num: str) -> str:
    while num:
        if int(num[-1]) % 2 != 0:
            return num
        num = num[:-1]
    return num


assert largest_odd_number("52") == "5"
assert largest_odd_number("4206") == ""
assert largest_odd_number("35427") == "35427"
