# 222. Count Complete Tree Nodes — Easy
# https://leetcode.com/problems/count-complete-tree-nodes/
# Pattern: tree, recursive DFS
# Time: O(n) | Space: O(h)
# Problem (summary): count all nodes in a complete binary tree.
# Key idea (v1, simple): same template as #104, but add instead of max:
# 1 (current node) + left count + right count. Empty tree -> 0 (not None: None + 1 crashes).
# Mistakes hit: return None in base case; passing two arguments to a one-argument function.
#
# v2 (accepted, faster) — Time: O(log² n) | Space: O(log n)
# A PERFECT tree (all levels full) with h levels has 2**h - 1 nodes -> no need to count.
# Check it cheaply: walk only left (lh) and only right (rh) from root, counting levels with
# `while l:` / `while r:` (pointers l = root, r = root set BEFORE the loops). lh == rh -> perfect
# -> return 2 ** lh - 1. Otherwise fall back to 1 + left + right. In a complete tree at least one
# subtree is perfect at every level, so recursion only follows one path.
# Mistakes hit in v2: `while root.left` (never changes -> infinite loop, and skips a level);
# 2*h instead of 2 ** lh; recursion left ABOVE the height check (still O(n) — it must be in else).

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionSimple:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.countNodes(root.left)
        right = self.countNodes(root.right)

        return left + right + 1


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        lh, rh = 0, 0

        if not root:
            return 0

        l = root
        while l:
            l = l.left
            lh += 1

        r = root
        while r:
            r = r.right
            rh += 1

        if rh == lh:
            return 2 ** lh - 1
        else:
            left = self.countNodes(root.left)
            right = self.countNodes(root.right)
        return left + right + 1


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
    print(Solution().countNodes(build([1, 2, 3, 4, 5, 6])))  # 6
    print(Solution().countNodes(build([])))  # 0
    print(Solution().countNodes(build([1])))  # 1
    print(Solution().countNodes(build([1, 2, 3, 4, 5, 6, 7])))  # 7 (perfect -> formula)
    print(SolutionSimple().countNodes(build([1, 2, 3, 4, 5, 6])))  # 6
