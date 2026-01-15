"""You are given two integer arrays nums1 and nums2, both sorted in non-decreasing order,
along with two integers m and n, where:

m is the number of valid elements in nums1,
n is the number of elements in nums2.
The array nums1 has a total length of (m+n), with the first m elements containing the values to be merged,
and the last n elements set to 0 as placeholders.

Your task is to merge the two arrays such that the final merged array is also sorted in non-decreasing order and stored entirely within nums1.
You must modify nums1 in-place and do not return anything from the function.
"""

# two pointers O(m+n) time, no extra space. Trick is to merge backwards, using the
# placeholder slots to avoid overwriting or needing to store temporary data


def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:
    last, p1, p2 = m + n - 1, m - 1, n - 1
    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[last] = nums1[p1]
            p1 -= 1
        else:
            nums1[last] = nums2[p2]
            p2 -= 1
        last -= 1
    print(nums1)
    return nums1


assert merge(nums1=[0, 0], m=0, nums2=[1, 2], n=2) == [1, 2]
assert merge(nums1=[10, 20, 20, 40, 0, 0], m=4, nums2=[1, 2], n=2) == [
    1,
    2,
    10,
    20,
    20,
    40,
]
