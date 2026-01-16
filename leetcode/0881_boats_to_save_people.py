"""You are given an array people where people[i] is the weight of the ith person,
and an infinite number of boats where each boat can carry a maximum weight of limit.
Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person."""

# counting sort, then two pointers ~O(N) provided the range of weights isn't too large


# surprisingly, I hadn't come across counting sort before! Some quick notes on it:
# - can be very efficient for sorting nonnegative integers with small ranges
# - can also be used for any countable set, but needs a little extra thought to find a mapping from number to array index
# - cannot sort real numbers (or indeed any uncountable set) because it needs to use array indices to represent numbers
# - time scales with O(n + max(array)), so even if it's technically usable for floats, it's a bad idea
# - space scales in same way, so generally worse than 'proper' sorting algos.


def counting_sort(nums: list[int]) -> list[int]:
    """Sorts nonnegative integer array in O(n + max(array)) time."""
    freqs = [0] * (max(nums) + 1)
    for num in nums:
        freqs[num] += 1
    out = []
    for n, f in enumerate(freqs):
        out.extend([n] * f)
    return out


def num_boats(people: list[int], limit: int) -> int:
    people = counting_sort(people)
    left, right = 0, len(people) - 1
    boats = 0

    while left <= right:
        boats += 1
        heavy = people[right]
        right -= 1
        light = people[left]
        if (heavy + light) <= limit:
            left += 1

    return boats


assert num_boats(people=[5, 1, 4, 2], limit=6) == 2
assert num_boats(people=[1, 3, 2, 3, 2], limit=3) == 4
assert num_boats(people=[1, 2, 3, 4, 5, 6], limit=6) == 4
