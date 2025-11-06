"""Given a binary tree, determine if it is height-balanced."""

# recursive DFS, O(n), where n is number of nodes in the tree

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(root: Optional[TreeNode]) -> bool:
    # returns height or -1 if the tree is unbalanced
    def get_height(node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        lhs = get_height(node.left)
        rhs = get_height(node.right)

        # bubble up any previous imbalances
        if lhs == -1 or rhs == -1:
            return -1

        # check for imbalance here
        if abs(lhs - rhs) > 1:
            return -1
        return 1 + (max(lhs, rhs))

    return get_height(root) != -1
