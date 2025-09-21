"""Max area / container with most water.

Given an array, let array[x] = y be coordinates.
Find the two array indices which give the largest
area (hold the most water). Return this area.
"""

# two pointer solution, O(n) time, O(1) space


def max_area(heights: list[int]) -> int:
    left = 0
    right = len(heights) - 1
    best = 0

    while left < right:
        area = min(heights[left], heights[right]) * (right - left)
        best = max(best, area)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return best


assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert max_area([1, 1]) == 1
