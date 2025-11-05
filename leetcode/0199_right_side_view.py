"""Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom."""


# DFS, O(n), where n is number of nodes in the tree

import math
from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rhs_view(root: Optional[TreeNode]) -> list[int]:
    seen, stack = set(), [(root, 0, 0)]  # stack is tuples of node and their coords
    res = {}  # res[i] is rhs node at depth i
    bst = defaultdict(lambda: -math.inf)  # bst[i] is the x coord of res[i]
    while stack:
        node, x, y = stack.pop()
        if node and node not in seen:
            if x > bst[y]:
                res[y] = node.val
                bst[y] = x
            seen.add(node)
            stack.extend([(node.left, x - 1, y + 1)] if node.left else [])
            stack.extend([(node.right, x + 1, y + 1)] if node.right else [])
    # a bit sketchy since it relies on the values being in order, can use OrderedDict instead
    return list(res.values())
