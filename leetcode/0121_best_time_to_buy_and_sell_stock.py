"""Best time to buy and sell stock.

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

# O(n) time.


def max_profit(prices: list[int]) -> int:
    buy_price = prices[0]
    best_profit = 0

    for price in prices:
        profit = price - buy_price
        buy_price = min(price, buy_price)
        best_profit = max(profit, best_profit)
    return best_profit


assert max_profit([7, 1, 5, 3, 6, 4]) == 5
assert max_profit([7, 6, 4, 3, 1]) == 0
