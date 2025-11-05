"""Maximum Depth of Binary Tree.

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

# O(n), DFS where n is number of nodes in the tree

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: Optional[TreeNode]) -> int:
    seen, stack = set(), [(root, 1)]
    res = 0
    while stack:
        node, depth = stack.pop()
        if node and node not in seen:
            res = max(depth, res)
            seen.add(node)
            stack.extend([(node.left, depth + 1)] if node.left else [])
            stack.extend([(node.right, depth + 1)] if node.right else [])
    return res
