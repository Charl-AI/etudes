"""You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.
The digits are stored in reverse order, e.g. the number 321 is represented as 1 -> 2 -> 3 -> in the linked list.
Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Return the sum of the two numbers as a linked list.
"""

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


def add_two_numbers(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    head, old = ListNode(), 0
    out = head
    while l1 or l2:
        a = l1.val if l1 else 0
        b = l2.val if l2 else 0
        car = (a + b + old) // 10
        rem = (a + b + old) % 10

        out.next = ListNode(rem)
        old = car  # old remembers the carry from the last loop

        out = out.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    out.next = ListNode(old) if old != 0 else None  # add any remaining carry
    return head.next  # discard dummy node from head and return rest


# fmt: off
assert add_two_numbers(l1 = ListNode._from_list([1,2,3]), l2 = ListNode._from_list([4,5,6]))._to_list() == [5,7,9] # type: ignore
assert add_two_numbers(l1 = ListNode._from_list([9]), l2 = ListNode._from_list([9]))._to_list() == [8,1] # type: ignore
assert add_two_numbers(l1 = ListNode._from_list([9,9,9,9,9,9,9]), l2 = ListNode._from_list([9,9,9,9]))._to_list() == [8,9,9,9,0,0,0,1] # type: ignore
