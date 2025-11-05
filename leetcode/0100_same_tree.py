"""Given the roots of two binary trees p and q, write a function to check if they are the same or not."""


# DFS, O(n), where n is number of nodes in the tree

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]):
    seen, p_stack, q_stack = set(), [p], [q]

    while p_stack and q_stack:
        p_node, q_node = p_stack.pop(), q_stack.pop()
        if (p_node is None) ^ (q_node is None):
            return False  # XOR checks if the terms are different
        if p_node and q_node and p_node not in seen:
            if p_node.val != q_node.val:
                return False
            seen.add(p_node)
            p_stack.extend([p_node.left, p_node.right])
            q_stack.extend([q_node.left, q_node.right])
    return True
