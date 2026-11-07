# 230. Kth Smallest Element in a BST — Medium (NeetCode 150)
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Pattern: tree DFS collecting values into a shared self.result list, then sort
# Time: O(n log n) | Space: O(n)
# Problem (summary): return the k-th smallest value in the BST (k counted from 1).
# Key idea: helper visits every node and appends ITS OWN value to self.result; sort the list;
# the k-th smallest sits at index k - 1 (k is 1-indexed, Python lists are 0-indexed).
# Note: the extra sort() helper is unnecessary — self.result.sort() can be called directly.
# Mistakes hit: list[k] instead of list[k - 1]; recursive calls on root instead of
# root.left / root.right (infinite recursion); appended children's values / the node object
# instead of root.val; call arguments not matching the function definitions.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0

        self.result = []
        self.counter(root)
        self.sort(self.result)
        return self.result[k - 1]

    def sort(self, result):
        self.result.sort()

    def counter(self, root):
        if not root:
            return []

        left = self.counter(root.left)
        right = self.counter(root.right)

        self.result.append(root.val)


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
    print(Solution().kthSmallest(build([3, 1, 4, None, 2]), 1))  # 1
    print(Solution().kthSmallest(build([5, 3, 6, 2, 4, None, None, 1]), 3))  # 3
    print(Solution().kthSmallest(build([1]), 1))  # 1
