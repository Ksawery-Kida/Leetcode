# 938. Range Sum of BST — Easy
# https://leetcode.com/problems/range-sum-of-bst/
# Pattern: tree, recursive DFS returning a number (#700 search + #404 summing)
# Time: O(n) | Space: O(h) (recursion stack)
# Problem (summary): sum the values of all nodes with low <= val <= high.
# Key idea: empty -> 0 (a sum, not None). Recurse on both children passing low/high unchanged,
# add root.val if low <= root.val <= high (one chained comparison covers both ends).
# Return own value + left + right.
# Possible optimization (BST pruning, not used here): if root.val < low the whole left subtree
# is too small — skip it; if root.val > high skip the right subtree.
# Mistakes hit: base case returned None (None + int crashes); passed nodes instead of low/high;
# both calls on root.left; left/right not added; forgot low/high args (TypeError); then called
# on root itself (infinite recursion, same as #700); 3 separate ifs instead of <=.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        result = 0

        left = self.rangeSumBST(root.left, low, high)
        right = self.rangeSumBST(root.right, low, high)

        if low <= root.val <= high:
            result += root.val

        return result + left + right


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
    print(Solution().rangeSumBST(build([10, 5, 15, 3, 7, None, 18]), 7, 15))  # 32
    print(Solution().rangeSumBST(build([10, 5, 15, 3, 7, 13, 18, 1, None, 6]), 6, 10))  # 23
