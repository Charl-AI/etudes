"""There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.
You are given two integer arrays position and speed, both of length n,
where position[i] is the starting mile of the ith car and speed[i] is the speed of the ith car in miles per hour.

A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.
A car fleet is a single car or a group of cars driving next to each other. The speed of the car fleet is the minimum speed of any car in the fleet.

If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.
Return the number of car fleets that will arrive at the destination.
"""

# O(nlogn), sorting, then stack


# can also do this by doing a zip, then builtin sort using x[0] as the key
# I just wanted to practice sorting here.


def sort_fleet(position: list[int], speed: list[int]):
    """Jointly sort position and speed arrays by ascending position."""
    assert len(position) == len(speed)
    if len(position) <= 1:
        return position, speed

    pivot = position[len(position) // 2]

    left_pos, left_speed = [], []
    right_pos, right_speed = [], []
    middle_pos, middle_speed = [], []
    for i in range(len(position)):
        p, s = position[i], speed[i]
        if position[i] < pivot:
            left_pos.append(p)
            left_speed.append(s)
        if position[i] > pivot:
            right_pos.append(p)
            right_speed.append(s)
        if position[i] == pivot:
            middle_pos.append(p)
            middle_speed.append(s)

    out_l = sort_fleet(left_pos, left_speed)
    out_r = sort_fleet(right_pos, right_speed)
    return out_l[0] + middle_pos + out_r[0], out_l[1] + middle_speed + out_r[1]


def car_fleet(target: int, position: list[int], speed: list[int]) -> int:
    sorted_pos, sorted_speed = sort_fleet(position, speed)
    cur, res = [], 0
    for p, s in zip(reversed(sorted_pos), reversed(sorted_speed)):
        if not cur:
            cur = [(p, s)]  # starts new fleet
            res += 1
        else:
            fp, fs = cur[-1]
            t = (target - fp) / fs
            ds, dp = s - fs, fp - p
            if ds > 0 and dp / ds <= t:
                continue  # joins fleet
            else:
                cur = [(p, s)]  # starts a new fleet
                res += 1
    return res


assert car_fleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]) == 3
assert car_fleet(target=10, position=[4, 1, 0, 7], speed=[2, 2, 1, 1]) == 3
assert car_fleet(target=10, position=[0, 4, 2], speed=[2, 1, 3]) == 1
