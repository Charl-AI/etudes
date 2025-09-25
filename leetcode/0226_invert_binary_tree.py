"""Invert binary tree.

Given the root of a binary tree, invert the tree, and return its root.
"""

# DFS solution: O(n) space and time, where n is number of nodes in the tree
# I find the stack-based iterative dfs implementation the most intuitive,
# it's a good idea to be able to write it v. quickly on command.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return None

    seen = set()
    stack = [root]
    while stack:
        node = stack.pop()
        if node not in seen:
            seen.add(node)
            for child in [node.left, node.right]:
                if child is not None:
                    stack.append(child)
            tmp = node.left
            node.left = node.right
            node.right = tmp
    return root
