# 2331. Evaluate Boolean Binary Tree — Easy
# https://leetcode.com/problems/evaluate-boolean-binary-tree/
# Pattern: tree DFS, compute left + right recursively, then combine (like #98)
# Time: O(n) | Space: O(h)
# Problem (summary): leaves are 0 (False) / 1 (True), inner nodes are 2 (OR) / 3 (AND);
# return the boolean value of the whole tree.
# Key idea: a leaf returns its own value; an inner node evaluates both children recursively
# and combines them with `or` (2) or `and` (3).
# Mistakes hit: evaluateTree called the helper without `return` (always None); recursed into
# evaluateTree instead of helper; leaf check `not root.left and root.right` (needs `not` on both).
# Note: the later `if not root.left and not root.right` branch is never reached — every leaf
# is 0 or 1 and returns earlier.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.val == 1:
            return True
        elif root.val == 0:
            return False

        if not root.left and not root.right:
            return False
        else:
            left = self.evaluateTree(root.left)
            right = self.evaluateTree(root.right)

        if root.val == 2:
            return left or right
        else:
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
    print(Solution().evaluateTree(build([2, 1, 3, None, None, 0, 1])))  # True
    print(Solution().evaluateTree(build([0])))  # False
    print(Solution().evaluateTree(build([3, 1, 0])))  # False
