"""You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock.
However, you can buy it then immediately sell it on the same day.
Also, you are allowed to perform any number of transactions but can hold at most one share of the stock at any time.

Find and return the maximum profit you can achieve."""

# O(n), two possible approaches, either DP, or greedy based on the trick that
# all upward movement is captured by the optimal strategy. For practice, I do both.

import functools
import math


def max_profit_greedy(prices: list[int]) -> int:
    profit = 0
    last = math.inf
    for price in prices:
        if price > last:
            profit += int(price - last)
        last = price
    return profit


def max_profit_dp(prices: list[int]) -> int:
    @functools.cache
    def inner(idx, holding):
        if idx == len(prices):  # base case
            return 0

        # profit at day idx is max of:
        # - profit if do nothing (res)
        # - profit if we buy/sell now and continue
        res = inner(idx + 1, holding)
        if holding:
            res = max(res, prices[idx] + inner(idx + 1, False))
        else:
            res = max(res, -prices[idx] + inner(idx + 1, True))
        return res

    return inner(0, False)


assert max_profit_greedy(prices=[7, 1, 5, 3, 6, 4]) == 7
assert max_profit_greedy(prices=[1, 2, 3, 4, 5]) == 4

assert max_profit_dp(prices=[7, 1, 5, 3, 6, 4]) == 7
assert max_profit_dp(prices=[1, 2, 3, 4, 5]) == 4
