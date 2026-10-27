# 965. Univalued Binary Tree — Easy
# https://leetcode.com/problems/univalued-binary-tree/
# Pattern: tree, recursive DFS
# Time: O(n) | Space: O(h)
# Problem (summary): do all nodes in the tree have the same value?
# Key idea: each node compares itself with its children (only if the child exists:
# `root.left and root.left.val != root.val` -> False), then the answer is left AND right,
# so a mismatch found deeper travels back up.
# Mistakes hit: compared with a hardcoded 1 (an all-0 tree is univalued too); ignored the
# left/right results; compared a bool result (left) with a node (root.left) — same mix-up
# as in #112; `and if` is a SyntaxError; final `return True` swallowed a deeper False.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left = self.isUnivalTree(root.left)
        right = self.isUnivalTree(root.right)

        if root.left and root.left.val != root.val:
            return False

        elif root.right and root.right.val != root.val:
            return False

        return left and right


def build(values):
    """Build a tree from LeetCode level-order list."""
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
    print(Solution().isUnivalTree(build([1, 1, 1, 1, 1, None, 1])))  # True
    print(Solution().isUnivalTree(build([2, 2, 2, 5, 2])))  # False
    print(Solution().isUnivalTree(build([0, 0, 0])))  # True
    print(Solution().isUnivalTree(build([1, 1, 1, 1, 2])))  # False (deep mismatch)
