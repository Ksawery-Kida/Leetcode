# 530. Minimum Absolute Difference in BST — Easy
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/
# Pattern: inorder traversal of a BST -> sorted list (like #94, #230), then compare neighbours
# Time: O(n) | Space: O(n)
# Problem (summary): return the minimum absolute difference between the values of any two
# different nodes in a BST.
# Key idea: inorder on a BST gives the values in ascending order, and in a sorted list the
# smallest difference is always between two adjacent elements -> collect seen[i] - seen[i-1]
# and return the min.
# Mistakes hit: first coded max - min (read the task as maximum); used undefined names (seen
# instead of self.seen, loop variable x vs i); subtracted in the wrong order (negative
# differences) and started at i = 0 (seen[-1] wraps to the last element).

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.seen = []
        self.inorder(root)
        min_diff = []

        for i in range(1, len(self.seen)):
            min_diff.append(self.seen[i] - self.seen[i - 1])

        return min(min_diff)

    def inorder(self, root):
        if not root:
            return 0

        left = self.inorder(root.left)
        self.seen.append(root.val)
        right = self.inorder(root.right)


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
    print(Solution().getMinimumDifference(build([4, 2, 6, 1, 3])))  # 1
    print(Solution().getMinimumDifference(build([1, 0, 48, None, None, 12, 49])))  # 1
    print(Solution().getMinimumDifference(build([10, 5, 20])))  # 5
