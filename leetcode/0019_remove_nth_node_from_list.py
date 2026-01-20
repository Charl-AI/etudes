"""Given the head of a linked list, remove the nth node from the end of the list and return its head."""

# O(N)

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


def remove_nth_node(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    left, right = dummy, dummy.next

    for _ in range(n):  # expand rhs pointer to nth node
        assert right
        right = right.next

    # advance until rhs is at end and lhs is at insertion point
    while right and left:
        left = left.next
        right = right.next

    assert left
    left.next = left.next.next if left.next else None
    return dummy.next


# fmt: off
assert remove_nth_node(head=ListNode._from_list([1,2,3,4]), n=2)._to_list() == [1,2,4] # type: ignore
assert remove_nth_node(head=ListNode._from_list([1,2]), n=2)._to_list() == [2]  # type: ignore
assert remove_nth_node(head=ListNode._from_list([5]), n=1) is None
