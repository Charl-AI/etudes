"""Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order and use the same number multiple times.
"""

# O(2^target) backtracking (dfs)
# each subproblem has following rules:
# - if adjusted target is less than zero, we've overshot
# - if adjusted target is zero, we've got it
# - else repeat with backtracking.


def combination_sum(nums: list[int], target: int) -> list[list[int]]:
    res = []
    nums.sort()

    # tgt is remainder left of target,
    # cur is the current combination being tried
    def inner(idx, tgt, cur):
        if tgt < 0:
            return  # do nothing if we've overshot the target
        if tgt == 0:
            res.append(cur.copy())
            return  # if the combination is good, add to res

        for other in range(idx, len(nums)):
            cur.append(nums[other])
            inner(other, tgt - nums[other], cur)
            cur.pop()  # backtrack

    _ = inner(0, target, [])
    return res
