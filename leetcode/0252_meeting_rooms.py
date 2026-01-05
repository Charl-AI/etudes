"""Given an array of meeting time interval objects consisting of start and end times,
determine if a person could add all meetings to their schedule without any conflicts."""

# nlogn, sort by start time and check for overlaps


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    @classmethod
    def _from_tuple(cls, interval: tuple[int, int]):
        return cls(interval[0], interval[1])


def can_attend_meetings(intervals: list[Interval]) -> bool:
    intervals = sorted(intervals, key=lambda x: x.start)
    last_end = -1
    for curr in intervals:
        if curr.start < last_end:
            return False
        last_end = curr.end

    return True


assert not can_attend_meetings(
    intervals=list(map(lambda x: Interval._from_tuple(x), [(0, 30), (5, 10), (15, 20)]))
)
assert can_attend_meetings(
    intervals=list(map(lambda x: Interval._from_tuple(x), [(5, 8), (9, 15)]))
)
