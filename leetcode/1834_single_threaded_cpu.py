import dataclasses
import heapq


@dataclasses.dataclass
class Task:
    idx: int
    enqueue_time: int
    processing_time: int

    def __lt__(self, other):
        if self.processing_time == other.processing_time:
            return self.idx < other.idx  # tiebreaker
        return self.processing_time < other.processing_time


def get_order(tasks: list[list[int]]) -> list[int]:
    if not tasks:
        return []

    # O(n) construct task objects
    task_list = []
    for i, t in enumerate(tasks):
        task_list.append(Task(i, t[0], t[1]))

    # O(nlogn) sort by enqueue_time
    task_list = sorted(task_list, key=lambda t: t.enqueue_time)

    time = task_list[0].enqueue_time
    heap = []
    res = []

    i, n = 0, len(task_list)
    while i < n or heap:
        # if CPU is idle, fast forward to next enqueue time
        if not heap and time < task_list[i].enqueue_time:
            time = task_list[i].enqueue_time

        # push all queued tasks onto the heap
        while i < n and task_list[i].enqueue_time <= time:
            heapq.heappush(heap, task_list[i])
            i += 1

        # process the task with the shortest processing time on the heap
        todo = heapq.heappop(heap)
        res.append(todo.idx)
        time += todo.processing_time

    return res
