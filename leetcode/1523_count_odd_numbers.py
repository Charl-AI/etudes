def count_odds(low: int, high: int) -> int:
    range = high - low
    return range // 2 + int(low % 2 != 0 or high % 2 != 0)


assert count_odds(3, 7) == 3
assert count_odds(8, 10) == 1
assert count_odds(14, 17) == 1
