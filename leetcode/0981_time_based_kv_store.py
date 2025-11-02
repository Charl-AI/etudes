"""Design a time-based key-value data structure that can store multiple values
for the same key at different time stamps and retrieve the key's value at a certain timestamp.
"""

from collections import defaultdict


class TimeMap:
    def __init__(self):
        # maps keys to list of tuples of (value,timestamp)
        self.data: dict[str, list[tuple[str, int]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values: list[tuple[str, int]] = self.data[key]
        if values == []:
            return ""

        lhs = 0
        rhs = len(values)
        res = ""

        while lhs < rhs:
            idx = lhs + (rhs - lhs) // 2
            val = values[idx]
            if val[1] == timestamp:
                return val[0]
            elif val[1] < timestamp:
                lhs = idx + 1
                res = val[0]
            elif val[1] > timestamp:
                rhs = idx
            else:
                raise ValueError("Something went wrong")
        return res
