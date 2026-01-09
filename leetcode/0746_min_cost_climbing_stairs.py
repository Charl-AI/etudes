"""You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor."""

# O(n) dynamic programming


def min_cost_climbing_stairs(cost: list[int]) -> int:
    memo = {}

    def inner(x):
        if x >= len(cost):
            return 0
        if x in memo:
            return memo[x]

        res = cost[x] + min(inner(x + 1), inner(x + 2))
        memo[x] = res
        return res

    return min(inner(0), inner(1))


assert min_cost_climbing_stairs([10, 15, 20]) == 15
assert min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
