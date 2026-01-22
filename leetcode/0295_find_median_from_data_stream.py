"""Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
"""

# O(log n) time for addNum, O(1) time for findMedian. Two heaps approach.

import heapq


class Heap:
    """Helper wrapper to make max-heaps easier (not builtin in python)."""

    def __init__(self, min: bool):
        self.lst = []
        self.sign = 1 if min else -1

    def push(self, num: int) -> None:
        heapq.heappush(self.lst, self.sign * num)

    def pop(self) -> int:
        return self.sign * heapq.heappop(self.lst)

    def peek(self) -> int:
        return self.sign * self.lst[0]

    def __len__(self) -> int:
        return len(self.lst)


class MedianFinder:
    def __init__(self):
        self.upper = Heap(min=True)  # min-heap for upper half of list
        self.lower = Heap(min=False)  # max-heap for lower half of list

    def addNum(self, num: int) -> None:
        if len(self.lower) != 0 and num < self.lower.peek():
            self.lower.push(num)
        else:
            self.upper.push(num)

        # rebalance heaps if differ by more than 1
        if len(self.lower) + 1 < len(self.upper):
            x = self.upper.pop()
            self.lower.push(x)
        elif len(self.upper) + 1 < len(self.lower):
            x = self.lower.pop()
            self.upper.push(x)
        assert abs(len(self.lower) - len(self.upper)) <= 1

    def findMedian(self) -> float:
        if len(self.upper) > len(self.lower):
            med = self.upper.peek()
        elif len(self.upper) < len(self.lower):
            med = self.lower.peek()
        else:
            med = (self.upper.peek() + self.lower.peek()) / 2.0

        return med


# fmt: off
mf = MedianFinder()
_ = mf.addNum(1)     #  arr = [1]
a = mf.findMedian()  # return 1.0
_ = mf.addNum(3)     # arr = [1, 3]
b = mf.findMedian()  # return 2.0
_ = mf.addNum(2)     # arr[1, 2, 3]
c = mf.findMedian()  # return 2.0

assert a == 1.0
assert b == 2.0
assert c == 2.0
