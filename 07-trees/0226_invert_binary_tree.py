# 226. Invert Binary Tree — Easy
# https://leetcode.com/problems/invert-binary-tree/
# Pattern: tree, recursive DFS
# Time: O(n) | Space: O(h) (recursion stack)
# Problem (summary): mirror the tree (swap left and right children in every node), return root.
# Key idea: same recursion template as #104, but nothing is counted — base case returns None
# (the function returns a node, not a number), recurse into both children, swap with
# root.left, root.right = root.right, root.left (Python tuple swap; `left = right` alone
# would overwrite and lose the original left). Return root.
# Note: left/right variables are unused — plain self.invertTree(root.left) calls are enough.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.right, root.left = root.left, root.right
        return root


def build(values):
    """Build a tree from LeetCode level-order list, e.g. [4, 2, 7, 1, 3, 6, 9]."""
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


def to_list(root):
    """Level-order list (trailing Nones trimmed), LeetCode style."""
    out, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            out.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            out.append(None)
    while out and out[-1] is None:
        out.pop()
    return out


if __name__ == "__main__":
    print(to_list(Solution().invertTree(build([4, 2, 7, 1, 3, 6, 9]))))  # [4, 7, 2, 9, 6, 3, 1]
    print(to_list(Solution().invertTree(build([2, 1, 3]))))  # [2, 3, 1]
    print(to_list(Solution().invertTree(build([]))))  # []
