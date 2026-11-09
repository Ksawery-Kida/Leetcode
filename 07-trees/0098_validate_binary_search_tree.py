# 98. Validate Binary Search Tree — Medium (NeetCode 150)
# https://leetcode.com/problems/validate-binary-search-tree/
# Pattern: tree DFS with BOUNDS passed down as arguments (low, high)
# Time: O(n) | Space: O(h)
# Problem (summary): check that every node is strictly greater than ALL nodes in its left
# subtree and strictly smaller than ALL nodes in its right subtree.
# Key idea: checking only parent vs child is not enough ([5,4,6,null,null,3,7]: 3 < 6 locally,
# but 3 sits in 5's right subtree). Each node gets an allowed range (low, high) from above:
# going left, high becomes root.val; going right, low becomes root.val. A node checks only
# itself (low < root.val < high); children check themselves. Start with (-inf, inf).
# Mistakes hit: comparison signs reversed; root.left.val before checking root.left exists;
# only parent-child checks; a single path max (one bound) instead of two; start bounds 0, 0;
# recursion results ignored; two return statements in a row (second one never runs).

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        low, high = float('-inf'), float('inf')

        return self.helper(root, low, high)

    def helper(self, root, low, high):
        # base cases lokalne
        if not root:
            return True

        if not (low < root.val < high):
            return False

        # rekurencja
        left = self.helper(root.left, low, root.val)
        right = self.helper(root.right, root.val, high)

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
    print(Solution().isValidBST(build([2, 1, 3])))  # True
    print(Solution().isValidBST(build([5, 1, 4, None, None, 3, 6])))  # False
    print(Solution().isValidBST(build([5, 4, 6, None, None, 3, 7])))  # False
    print(Solution().isValidBST(build([2, 2, 2])))  # False (duplicates)
    print(Solution().isValidBST(build([-2147483648])))  # True
