"""You are given an integer array coins representing coins of different denominations
(e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.

Return the fewest number of coins that you need to make up the exact target amount.
If it is impossible to make up the amount, return -1."""

# dynamic programming O(len(coins) * amount). For each amount, try every coin
# and solve the subproblem for amount - coin. Note that the greedy solution
# of always using the largest coin doesn't work.

import math


def get_min_pos(arr: list[int]) -> int:
    # get the smallest positive number, or -1 if all negative
    best = math.inf
    for num in arr:
        if num < best and num > 0:
            best = int(num)
    return best if best is not math.inf else -1  # type: ignore


def coin_change(coins: list[int], amount: int) -> int:
    if amount == 0:
        return 0
    memo = [0 for _ in range(amount + 1)]

    def inner(n):
        if n in set(coins):
            return 1  # if amount is a coin, base case 1
        if n < min(coins):
            return -1  # if amount is smaller than smallest coin, impossible
        if memo[n] != 0:
            return memo[n]  # get cached answer

        # try to solve with all choices of coin
        res = [inner(n - coin) + 1 for coin in coins]
        out = get_min_pos(res)
        memo[n] = out
        return out

    return inner(amount)


assert coin_change(coins=[1, 5, 10], amount=12) == 3
assert coin_change(coins=[2], amount=3) == -1
assert coin_change(coins=[1], amount=0) == 0
assert coin_change(coins=[1, 2, 5], amount=100) == 20
