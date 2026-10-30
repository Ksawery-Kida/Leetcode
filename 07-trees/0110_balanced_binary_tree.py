# 110. Balanced Binary Tree — Easy (NeetCode 150)
# https://leetcode.com/problems/balanced-binary-tree/
# Pattern: tree, recursion + helper (maxDepth copied from #104)
# Time: O(n^2) worst (maxDepth recomputed at every node) | Space: O(h)
# Problem (summary): height-balanced = at EVERY node the heights of the left and right subtrees
# differ by at most 1.
# Key idea: isBalanced returns a bool, so it can't give heights -> add helper maxDepth (#104,
# base case 0). At each node: compare self.maxDepth(root.left) vs self.maxDepth(root.right)
# (diff > 1 -> False), AND both subtrees must be balanced themselves (isBalanced on children)
# — checking only the root is not enough. Empty tree -> True.
# Faster O(n) version (later): one helper returning height or -1 for "unbalanced".
# Mistakes hit: base case False/None instead of True; used the bool results as heights
# (left - right); height_left += 1 (local var, always 1 — height must come FROM BELOW);
# maxDepth without base case / returning True instead of 0; self.maxDepth() without an arg;
# child-balance check as two ifs (missed the both-False case) -> one `not left or not right`.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        height_left = self.maxDepth(root.left)
        height_right = self.maxDepth(root.right)

        left = self.isBalanced(root.left)

        right = self.isBalanced(root.right)

        if height_left - height_right > 1:
            return False

        elif height_right - height_left > 1:
            return False

        if not left or not right:
            return False

        return True

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)


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
    print(Solution().isBalanced(build([3, 9, 20, None, None, 15, 7])))  # True
    print(Solution().isBalanced(build([1, 2, 2, 3, 3, None, None, 4, 4])))  # False
    print(Solution().isBalanced(build([])))  # True
    print(Solution().isBalanced(build([1, 2, 2, 3, None, None, 3, 4, None, None, 4])))  # False (root OK, children not)
