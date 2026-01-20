"""Design and implement a data structure for a Least Frequently Used (LFU) cache."""

# cache itself is a hashmap, with auxiliary doubly linked list
# we use an auxiliary dict mapping frequencies to LRUCaches for each frequency
# we could use the LRUCache implementation from the previous problem, but we can
# also use Python's builtin OrderedDict for an easier option.

from collections import OrderedDict, defaultdict
from dataclasses import dataclass, field


@dataclass
class LRUCache:
    cache: OrderedDict = field(default_factory=OrderedDict)

    def __len__(self):
        return len(self.cache)

    def put(self, key: int, value: int):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value

    def remove(self, key: int):
        _ = self.cache.pop(key)

    def pop_lru(self):
        return self.cache.popitem(last=False)


@dataclass
class Item:
    key: int
    val: int
    frq: int


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache, self.lrus = {}, defaultdict(LRUCache)
        self.min_frq = 0

    def _access(self, key):
        """Access an item to increment its count and position in lrus."""
        if key not in self.cache:
            return None

        item = self.cache[key]
        self.lrus[item.frq].remove(key)

        # increment global min_frq if necessary
        if item.frq == self.min_frq and len(self.lrus[item.frq]) == 0:
            self.min_frq += 1
        item.frq += 1

        self.lrus[item.frq].put(key, item.val)
        return item

    def get(self, key: int) -> int:
        item = self._access(key)
        return item.val if item else -1

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        item = self._access(key)
        if item:
            item.val = value
            self.lrus[item.frq].put(key, value)

        elif len(self.cache) < self.capacity:
            item = Item(key, value, 0)
            self.cache[key] = item
            self.lrus[0].put(key, value)
            self.min_frq = 0
        else:
            last = self.lrus[self.min_frq].pop_lru()
            del self.cache[last[0]]
            item = Item(key, value, 0)
            self.cache[key] = item
            self.lrus[0].put(key, value)
            self.min_frq = 0


# fmt: off
cache = LFUCache(2)
_ = cache.put(1, 1)
_ = cache.put(2, 2)
a = cache.get(1)     # a = 1
_ = cache.put(3, 3)  # eject key 2
b = cache.get(2)     # b = -1
c = cache.get(3)     # c = 3
_ = cache.put(4,4)   # eject key 1
d = cache.get(1)     # d = -1
e = cache.get(3)     # e = 3
f = cache.get(4)     # f = 4


assert a == 1
assert b == -1
assert c == 3
assert d == -1
assert e == 3
assert f == 4
