"""A linked list of length n is given such that each node contains an additional random pointer,
which could point to any node in the list, or null.

Construct a deep copy of the list.
The deep copy should consist of exactly n brand new nodes,
where each new node has its value set to the value of its corresponding original node.
Both the next and random pointer of the new nodes should point to new nodes in the
copied list such that the pointers in the original list and copied list represent the same list state.
None of the pointers in the new list should point to nodes in the original list.
"""


# O(N) -- two passes. First create the copy without the extra pointer and build a hashmap to
# remember each node. Then add the pointers in the second pass. We do it this way because
# the random pointers may point to nodes we haven't created yet.

from typing import Optional


class Node:
    def __init__(
        self, x: int, next: Optional["Node"] = None, random: Optional["Node"] = None
    ):
        self.val = int(x)
        self.next = next
        self.random = random


def copy_random_list(head: Optional["Node"]) -> Optional["Node"]:
    if not head:
        return None
    node_map = {}  # maps nodes from old list to corresponding nodes in new list

    # First pass: Create all new nodes and store them in the hash map
    curr = head
    while curr:
        node_map[curr] = Node(curr.val)
        curr = curr.next

    # Second pass: Wire up the next and random pointers
    curr = head
    while curr:
        node_map[curr].next = node_map.get(curr.next)  # .get() safely handles None's
        node_map[curr].random = node_map.get(curr.random)
        curr = curr.next

    return node_map[head]
