"""Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree."""

# O(h) where h is the height of the tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lca(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    curr = root
    lo = min(p.val, q.val)
    hi = max(p.val, q.val)
    while curr:
        if lo <= curr.val <= hi:
            return curr
        elif hi < curr.val:
            curr = curr.left
        elif lo > curr.val:
            curr = curr.right
        else:
            raise ValueError("Something went wrong")
    raise ValueError("No lca found")
