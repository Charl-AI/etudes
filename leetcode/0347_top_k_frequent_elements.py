"""Top K frequent elements.

Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.
"""

from collections import defaultdict


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    freqs = defaultdict(int)
    for num in nums:
        freqs[num] += 1

    # buckets[i] holds all numbers with frequency i
    # we know that the frequency can't exceed the
    # length of nums, so we only need that many buckets
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in freqs.items():
        buckets[freq].append(num)

    result = []
    while len(result) <= k:
        for bucket in reversed(buckets):
            result.extend(bucket)
    return result[:k]


assert top_k_frequent(nums=[1, 1, 1, 2, 2, 3], k=2) == [1, 2]
assert top_k_frequent(nums=[1], k=1) == [1]
assert top_k_frequent(nums=[1, 2, 1, 2, 1, 2, 3, 1, 3, 2], k=2) == [1, 2]
