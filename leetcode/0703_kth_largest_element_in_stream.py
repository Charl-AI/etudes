"""You are tasked to implement a class which, for a given integer k,
maintains a stream of test scores and continuously returns the kth
highest test score after a new score has been submitted.
More specifically, we are looking for the kth highest score in the sorted list of all scores.
"""

# min heap of top k elements using builtin heapq
# O(len(nums)) initial heapify, then O(log k) push and O(1) get min

import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap, self.k = nums, k
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            _ = heapq.heappop(self.heap)
        return self.heap[0]
