"""Given an array of points where points[i] = [xi, yi]
represents a point on the X-Y plane and an integer k,
return the k closest points to the origin (0, 0).
"""

# O(nlogk) max heap

import dataclasses
import heapq
import math


@dataclasses.dataclass
class Point:
    x: int
    y: int
    d: float

    def __lt__(self, other):
        # flipped comparison sign to use as max heap
        return self.d > other.d


def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    heap: list[Point] = []
    heapq.heapify(heap)

    for x, y in points:
        d = math.sqrt(x**2 + y**2)
        p = Point(x, y, d)
        heapq.heappush(heap, p)
        while len(heap) > k:
            _ = heapq.heappop(heap)

    return [[p.x, p.y] for p in heap]
