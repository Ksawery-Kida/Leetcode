# 404. Sum of Left Leaves — Easy
# https://leetcode.com/problems/sum-of-left-leaves/
# Pattern: tree, recursive DFS returning a number (like #222: 1 + left + right)
# Time: O(n) | Space: O(h) (recursion stack)
# Problem (summary): sum the values of all leaves that are the LEFT child of their parent.
# Key idea: a node doesn't know if it's a left or right child, so stand on the PARENT and look
# down at root.left: it exists AND has no children of its own (root.left.left / root.left.right)
# -> it's a left leaf, take root.left.val. Answer = (that value or 0) + left + right.
# The right subtree must be recursed too — it can contain left leaves (15 under 20 below).
# Mistakes hit: wanted to skip the right recursion; root.left (node) instead of root.left.val;
# leaf check on root instead of root.left; SumOfLeftLeaves (capital S) and passing 2 args;
# root.right.left instead of root.left.right (AttributeError when root.right is None).
# Heavily hinted (leaf-check line given) -> REDO from scratch in a few days, also a list version.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:  # base case
            return 0

        outcome = 0

        left = self.sumOfLeftLeaves(root.left)  # rekurencja
        right = self.sumOfLeftLeaves(root.right)

        if root.left and not root.left.left and not root.left.right:  # sprawdzam czy node jest listkiem
            outcome += root.left.val

        return outcome + left + right


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
    print(Solution().sumOfLeftLeaves(build([3, 9, 20, None, None, 15, 7])))  # 24
    print(Solution().sumOfLeftLeaves(build([1])))  # 0
    print(Solution().sumOfLeftLeaves(build([1, 2, 3, 4, 5])))  # 4
