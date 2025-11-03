"""Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days
you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.
"""

# stack-based, O(n) time. Quite tricky imo


def daily_temperatures(temperatures: list[int]) -> list[int]:
    result = [0 for _ in range(len(temperatures))]
    stack: list[tuple[int, int]] = []  # (temp,index)

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            _, idx = stack.pop()
            result[idx] = i - idx
        stack.append((t, i))
    return result


assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
assert daily_temperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
assert daily_temperatures([30, 60, 90]) == [1, 1, 0]
