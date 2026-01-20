"""Implement the Least Recently Used (LRU) cache class LRUCache."""

# cache itself is a hashmap, with auxiliary doubly linked list
# to help track which keys are recently used.
# get() and put() may thus run in O(1) time.

import dataclasses
import typing


@dataclasses.dataclass
class ListNode:
    key: int
    val: int
    lhs: typing.Optional["ListNode"] = None  # lhs node should be more recently used
    rhs: typing.Optional["ListNode"] = None  # rhs node should be less recently used


# NB, each linked list operation we assert the following invariant:
# assert not (self.head is None) ^ (self.tail is None)
# i.e. head and tail must either both be None or both be Nodes


@dataclasses.dataclass
class DoubleLinkedList:
    head: typing.Optional[ListNode] = None  # head stores most recently used (lhs)
    tail: typing.Optional[ListNode] = None  # tail stores least recently used (rhs)

    def remove(self, node: ListNode):
        assert not ((self.head is None) ^ (self.tail is None))
        if node is self.head:
            self.head = node.rhs
        if node is self.tail:
            self.tail = node.lhs

        if node.lhs:
            node.lhs.rhs = node.rhs
        if node.rhs:
            node.rhs.lhs = node.lhs

    def pop_tail(self):
        assert not ((self.head is None) ^ (self.tail is None))
        if not self.tail:
            return None
        tail = ListNode(self.tail.key, self.tail.val)
        self.remove(self.tail)
        return tail

    def insert_left(self, node: ListNode):
        assert not ((self.head is None) ^ (self.tail is None))
        if self.head:
            self.head.lhs = node
            node.rhs, node.lhs = self.head, None
            self.head = node
        else:
            self.head, self.tail = node, node


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.list = DoubleLinkedList()

    def get(self, key: int) -> int:
        """Returns -1 if key not in cache, else returns cached value and
        makes key the MRU (i.e. head of the list)."""

        node = self.cache.get(key, None)
        if not node:
            return -1

        self.list.remove(node)
        self.list.insert_left(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        """Adds/updates the key in the cache and makes the key the MRU
        (i.e. head of the list). If the cache now exceeds capacity, ejects
        LRI (i.e. tail of the list)."""

        if self.capacity <= 0:
            return

        # remove if already in cache so we can move it to front
        if key in self.cache:
            self.list.remove(self.cache[key])

        # add node to MRU position
        node = ListNode(key, value)
        self.list.insert_left(node)
        self.cache[key] = node

        # eject LRU if too long now
        if len(self.cache) > self.capacity:
            last = self.list.pop_tail()
            if last and self.cache.get(last.key) is not None:
                del self.cache[last.key]


# fmt: off
lRUCache = LRUCache(2)
_ = lRUCache.put(1, 10)   # cache: {1=10}
x = lRUCache.get(1)       # return 10
_ = lRUCache.put(2, 20)   # cache: {1=10, 2=20}
_ = lRUCache.put(3, 30)   # cache: {2=20, 3=30}, key=1 was evicted
y = lRUCache.get(2)       # returns 20
z = lRUCache.get(1)       # return -1 (not found)

assert x == 10
assert y == 20
assert z == -1
