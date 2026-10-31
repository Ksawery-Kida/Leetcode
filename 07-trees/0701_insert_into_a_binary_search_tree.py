# 701. Insert into a Binary Search Tree — Medium
# https://leetcode.com/problems/insert-into-a-binary-search-tree/
# Pattern: BST, recursive search one way (#700) + attaching the recursion result (#617)
# Time: O(h) — O(log n) balanced, O(n) skewed | Space: O(h) (recursion stack)
# Problem (summary): insert val into a BST so it stays a BST; return the root.
# Key idea: go down like #700 (compare val with root.val) until you hit an EMPTY spot — that
# empty spot is the base case: return TreeNode(val) (CREATE a node). The parent attaches it via
# root.left = self.insertIntoBST(root.left, val) (or right). Every level returns its own root,
# so unchanged parts get re-attached to themselves and the top call returns the whole tree.
# Mistakes hit: base case returned 0; compared root.left.val instead of root.val; `value` vs val;
# base case moved to the bottom (root.val on None crashes); self.insertIntoBST(val) instead of
# TreeNode(val) (calling vs creating — reverse of the #617 mistake); results in loose left/right
# variables (new node lost); typo root.tright.
# Redo 2026-10-31: rewritten from scratch, correct on first try (two ifs instead of if/elif — fine,
# they're mutually exclusive). Walked through the insert-5 trace: TreeNode(val) CREATES the node,
# return HANDS it to the parent, parent ATTACHES it via root.left/right = ...

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)

        elif root.val < val:
            root.right = self.insertIntoBST(root.right, val)

        return root


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
    print(to_list(Solution().insertIntoBST(build([4, 2, 7, 1, 3]), 5)))  # [4, 2, 7, 1, 3, 5]
    print(to_list(Solution().insertIntoBST(build([]), 5)))  # [5]
    print(to_list(Solution().insertIntoBST(build([4, 2, 7]), 1)))  # [4, 2, 7, 1]
