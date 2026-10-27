# O(log n) simulate the water bottle drinking and exchange process


def num_water_bottles(num_bottles: int, num_exchange: int) -> int:
    drank, empty = num_bottles, num_bottles

    traded, empty = divmod(empty, num_exchange)
    while traded > 0:
        drank += traded
        empty += traded
        traded, empty = divmod(empty, num_exchange)
    return drank


assert num_water_bottles(9, 3) == 13
assert num_water_bottles(15, 4) == 19

# NB, closed form O(1) is possible: num_bottles + (num_bottles - 1) // (num_exchange - 1)
