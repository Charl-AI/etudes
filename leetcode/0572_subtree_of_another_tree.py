"""Given the roots of two binary trees root and subRoot,
return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
The tree tree could also be considered as a subtree of itself.
"""

# DFS, O(n*,), where n,m are numbers of nodes in the trees

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# NB, I usually write DFS with a set to track seen nodes, but this is actually
# unnecessary in acyclic graphs like binary trees.


def tree_equal(root1: Optional[TreeNode], root2: Optional[TreeNode]):
    stack1, stack2 = [root1], [root2]
    while stack1:
        node1, node2 = stack1.pop(), stack2.pop()
        if (node1 is None) ^ (node2 is None):
            return False
        if node1 and node2:
            if node1.val != node2.val:
                return False
            stack1.extend([node1.left, node1.right])
            stack2.extend([node2.left, node2.right])
    return True


def is_subtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            if tree_equal(node, subRoot):
                return True
            stack.extend([node.left, node.right])
    return False
