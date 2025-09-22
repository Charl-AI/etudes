"""Reverse linked list.

Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

# O(n) time, O(1) space (in-place)

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # aux methods for tests, not actually used in the solution

    @classmethod
    def _from_list(cls, vals):
        head = cls(vals.pop(0))
        curr = head
        while vals:
            node = cls(vals.pop(0))
            curr.next = node
            curr = curr.next
        return head

    def _to_list(self):
        out = []
        curr = self
        while curr is not None:
            out.append(curr.val)
            curr = curr.next
        return out

    def __repr__(self) -> str:
        return str(self._to_list())


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head

    prev, curr = None, head
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


assert reverse_list(ListNode._from_list([1, 2, 3, 4]))._to_list() == [4, 3, 2, 1]  # type: ignore
assert reverse_list(ListNode._from_list([1, 2]))._to_list() == [2, 1]  # type: ignore
