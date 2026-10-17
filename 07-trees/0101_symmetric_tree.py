# 101. Symmetric Tree — Easy
# https://leetcode.com/problems/symmetric-tree/
# Pattern: tree, recursive DFS on two nodes at once (helper)
# Time: O(n) | Space: O(h) (recursion stack)
# Problem (summary): is the tree a mirror of itself around its center?
# Key idea: isSymmetric(root.left) alone is wrong (checks a subtree by itself). Need a helper
# isMirror(p, q) with two arguments — same base cases as #100 Same Tree (both None -> True,
# one None -> False, different val -> False), but the recursion is MIRRORED:
# p.left vs q.right (outer pair) and p.right vs q.left (inner pair). Both must be True.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root.left, root.right)

    def isMirror(self, p, q):
        if not p and not q:
            return True
        if p and not q:
            return False
        if q and not p:
            return False
        if p.val != q.val:
            return False
        left = self.isMirror(p.left, q.right)
        right = self.isMirror(p.right, q.left)
        if left and right:
            return True
        else:
            return False


def build(values):
    """Build a tree from LeetCode level-order list, e.g. [1, 2, 2, 3, 4, 4, 3]."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


if __name__ == "__main__":
    print(Solution().isSymmetric(build([1, 2, 2, 3, 4, 4, 3])))  # True
    print(Solution().isSymmetric(build([1, 2, 2, None, 3, None, 3])))  # False
    print(Solution().isSymmetric(build([1])))  # True
