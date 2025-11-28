"""You are given an array of CPU tasks,
each labeled with a letter from A to Z, and a number n.
Each CPU interval can be idle or allow the completion of one task.
Tasks can be completed in any order, but there's a constraint:
there has to be a gap of at least n intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.
"""

# max heap O(n)

import heapq
from collections import defaultdict, deque


def least_interval(tasks: list[str], n: int) -> int:
    neg_freqs = defaultdict(int)  # store negative freqs for max-heap
    for task in tasks:
        neg_freqs[task] -= 1

    heap, queue = list(neg_freqs.values()), deque([])
    heapq.heapify(heap)
    time = 0

    while heap or queue:
        if not heap:
            time, freq = queue.popleft()
            heapq.heappush(heap, freq)
        else:
            if queue and queue[0][0] <= time:
                _, freq = queue.popleft()
                heapq.heappush(heap, freq)

            freq = heapq.heappop(heap)
            freq += 1
            if freq != 0:
                queue.append((time + n, freq))

        time += 1

    return time
