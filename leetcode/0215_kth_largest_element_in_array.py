"""Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?
"""

# min heap of top k elements
# note, it's a bit too easy to solve this with the inbuilt heapq
# so I'll use this as practice for implementing my own


class MinHeap:
    def __init__(self):
        self.heap = []

    def __len__(self) -> int:
        return len(self.heap)

    def _bubble_up(self, idx: int):
        parent_idx = (idx - 1) // 2
        while idx > 0 and self.heap[idx] < self.heap[parent_idx]:
            self.heap[idx], self.heap[parent_idx] = (
                self.heap[parent_idx],
                self.heap[idx],
            )  # swap current and parent

            idx = parent_idx
            parent_idx = (idx - 1) // 2

    def _bubble_down(self, idx: int):
        n = len(self.heap)

        while True:
            smallest = idx
            left_child = 2 * idx + 1
            right_child = 2 * idx + 2

            if left_child < n and self.heap[left_child] < self.heap[smallest]:
                smallest = left_child

            if right_child < n and self.heap[right_child] < self.heap[smallest]:
                smallest = right_child

            if smallest == idx:
                break

            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            idx = smallest

    def push(self, num: int):
        self.heap.append(num)
        self._bubble_up(len(self.heap) - 1)

    def pop(self) -> int:
        if len(self.heap) == 1:
            root = self.heap[0]
            self.heap = []
            return root

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return root


def kth_largest(nums: list[int], k: int) -> int:
    h = MinHeap()
    for num in nums:
        h.push(num)

        while len(h) > k:
            h.pop()
    return h.pop()
