"""Given a list of nums length n with range [1,n],
return the duplicate number. Remember there must always be
at least one duplicate due to the pidgeonhole principle."""

# O(n) time, easy with O(n) space, but we do it with O(1)
# space by using Floyd's cycle detection algorithm
# (fast/slow pointers, treating the indices like a linked list)


def find_duplicate(nums: list[int]) -> int:
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]  # goto the index that the number in this slot points to
        fast = nums[nums[fast]]  # same, but two steps in one go
        if slow == fast:
            break

    # now find the entrance to the cycle
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return fast


assert find_duplicate(nums=[1, 2, 3, 2, 2]) == 2
assert find_duplicate(nums=[1, 2, 3, 4, 4]) == 4
