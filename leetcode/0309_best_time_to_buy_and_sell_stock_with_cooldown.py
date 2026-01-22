"""You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve.
You may complete as many transactions as you like with the following restriction:
After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
"""

# O(n) with dynamic programming

import functools


def max_profit(prices: list[int]) -> int:
    @functools.cache
    def inner(idx, holding):
        if idx >= len(prices):  # base case
            return 0
        if holding:
            return max(
                inner(idx + 1, holding),  # do nothing and decide tomorrow
                inner(idx + 2, False)
                + prices[idx],  # sell and potentially buy on day + 2
            )
        else:
            return max(
                inner(idx + 1, holding),  # do nothing and decide tomorrow
                inner(idx + 1, True)
                - prices[idx],  # buy and potentially sell on day + 1
            )

    return inner(0, False)


assert max_profit(prices=[1, 3, 4, 0, 4]) == 6
assert max_profit(prices=[1, 2, 3, 0, 2]) == 3
assert max_profit(prices=[1]) == 0
