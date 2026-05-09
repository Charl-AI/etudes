# O(n) time with two pointers. We will use the left pointer to keep track of how many unique
# elements we've found. The right pointer moves ahead. When the right pointer finds a new element,
# we increment the left pointer and copy the element to the new left pointer position.
# If we wished to access the list with duplicates removed, we could simply then slice
# off everything after the left pointer at the end.


def remove_duplicates(nums: list[int]) -> int:
    lhs = 1  # start at 1, since first element is always unique

    for rhs in range(1, len(nums)):
        # take advantage of the fact that duplicates are consecutive in sorted lists
        if nums[rhs] != nums[rhs - 1]:
            nums[lhs] = nums[rhs]
            lhs += 1

    print(nums[:lhs])  # print final array with duplicates removed
    return lhs


assert remove_duplicates(nums=[2, 10, 10, 30, 30, 30]) == 3  # prints [2,10,30]
