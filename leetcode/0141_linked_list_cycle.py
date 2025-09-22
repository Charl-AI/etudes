"""Linked list cycle.

Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can
be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""

# O(n) time. You can use a hashmap/set to do it in O(n) space,
# or use the fast/slow pointers trick to do it in O(1) space.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head: Optional[ListNode]) -> bool:
    if head is None or head.next is None:
        return False

    slow = head
    fast = head

    while slow is not None and fast is not None:
        if fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next
        if id(slow) == id(fast):
            return True
    return False
