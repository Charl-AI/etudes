def calculate_money(n: int) -> int:
    weeks, days = n // 7, n % 7

    # each subsequent week contributes 7 more than week 1
    week_1, week_n = 28, 28 + 7 * (weeks - 1)

    res = weeks * (week_1 + week_n) // 2  # arithmetic series

    # add on final week (O(1) due to only up to 7 iterations)
    for day in range(days):
        res += day + weeks + 1
    return res


assert calculate_money(4) == 10
assert calculate_money(10) == 37
assert calculate_money(20) == 96
