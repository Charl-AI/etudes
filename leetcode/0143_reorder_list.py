"""Reorder list.

The positions of a linked list of length = 7 for example, can intially be represented as:
[0, 1, 2, 3, 4, 5, 6]
Reorder the nodes of the linked list to be in the following order:
[0, 6, 1, 5, 2, 4, 3]
Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:
[0, n-1, 1, n-2, 2, n-3, ...]
You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.
"""

# O(n) time, O(1) space. The trick here is to first find the midpoint, then split and reverse the
# second half, then merge the two halves. The midpoint can be found with the fast/slow pointer trick

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorder_list(head: Optional[ListNode]) -> None:
    if head is None or head.next is None:
        return

    # find midpoint
    slow, fast = head, head.next
    while fast and fast.next:
        assert slow is not None
        slow = slow.next
        fast = fast.next.next

    assert slow is not None
    curr = slow.next
    slow.next = None  # chop off second half
    prev = None

    while curr is not None:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp

    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2
