"""A conveyor belt has packages that must be shipped from one port to another within days days.
The ith package on the conveyor belt has a weight of weights[i].
Each day, we load the ship with packages on the conveyor belt (in the order given by weights).
We may not load more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.
"""

# binary search solution with O(n) inner loop -> ~nlogn
# you can do the binary search manually fairly easily but I've
# used the builtin bisect module with a lazy map class for practice.

import bisect


def _can_ship(weights: list[int], days: int, capacity: int) -> bool:
    ships, current_cap = 1, capacity

    for w in weights:
        if current_cap - w < 0:
            ships += 1
            if ships > days:
                return False
            current_cap = capacity
        current_cap -= w
    return True


class LazyMap:
    def __init__(self, arr, map_fn):
        self.arr = arr
        self.map_fn = map_fn

    def __len__(self):
        return len(self.arr)

    def __getitem__(self, idx: int):
        return self.map_fn(self.arr[idx])


def ship_within_days(weights: list[int], days: int) -> int:
    # smallest possible capacity is the largest weight in weights
    # biggest useful capacity is sum(weights) so it always does it in one day.
    capacities = range(max(weights), sum(weights) + 1)

    # for capacity[i], can_ship[i] is a bool for whether it can ship in the given days
    can_ship = LazyMap(capacities, lambda cap: _can_ship(weights, days, cap))
    idx = bisect.bisect_left(can_ship, True)
    return capacities[idx]


assert ship_within_days(weights=[2, 4, 6, 1, 3, 10], days=4) == 10
