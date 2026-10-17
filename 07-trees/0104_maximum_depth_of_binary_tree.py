# 104. Maximum Depth of Binary Tree — Easy
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Pattern: tree, recursive DFS
# Time: O(n) | Space: O(h) (recursion stack, h = tree height)
# Problem (summary): return the number of nodes on the longest root-to-leaf path.
# Key idea: recursion template — base case `if not root: return 0` (empty tree has depth 0),
# trust that self.maxDepth(root.left/right) already works, combine: 1 + max(left, right)
# (the 1 is the current node's level; a leaf = 1 + max(0, 0) = 1).
# Gotchas hit: no `for x in tree` — recursion walks it; Python has None, not null;
# recursive call is self.maxDepth inside a class; call children only AFTER the base case.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)


def build(values):
    """Build a tree from LeetCode level-order list, e.g. [3, 9, 20, None, None, 15, 7]."""
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
    print(Solution().maxDepth(build([3, 9, 20, None, None, 15, 7])))  # 3
    print(Solution().maxDepth(build([1, None, 2])))  # 2
    print(Solution().maxDepth(build([])))  # 0
