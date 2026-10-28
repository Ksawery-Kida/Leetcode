# 700. Search in a Binary Search Tree — Easy
# https://leetcode.com/problems/search-in-a-binary-search-tree/
# Pattern: BST, recursive search going ONE way (binary search on a tree, like #704)
# Time: O(h) — O(log n) balanced, O(n) skewed | Space: O(h) (recursion stack)
# Problem (summary): return the node whose value is val (with its subtree), or None.
# Key idea: BST = everything in the left subtree is smaller, everything in the right is bigger.
# Base case: empty -> None. Found (root.val == val) -> return root (the node itself). Otherwise
# compare and go only one way, RETURNING the recursion result directly:
# return self.searchBST(root.left or root.right, val).
# Mistakes hit: passed nodes instead of val as the 2nd arg; recursed both ways (ignores BST);
# left.val on a result that can be None; returned a tuple of children; reassigned
# root.left = root.left.left (mutates the tree instead of going down); stored recursion results
# in unused variables + bare return; return self.searchBST(root, val) -> infinite recursion.
# BST fact to remember: inorder traversal (left -> node -> right) gives sorted values.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val == val:
            return root

        if root.val > val:
            return self.searchBST(root.left, val)

        elif root.val < val:
            return self.searchBST(root.right, val)


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


def to_list(root):
    """Tree -> LeetCode level-order list (trailing Nones trimmed)."""
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
    print(to_list(Solution().searchBST(build([4, 2, 7, 1, 3]), 2)))  # [2, 1, 3]
    print(to_list(Solution().searchBST(build([4, 2, 7, 1, 3]), 5)))  # []
