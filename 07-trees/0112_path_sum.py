# 112. Path Sum — Easy
# https://leetcode.com/problems/path-sum/
# Pattern: tree, recursive DFS passing a value down
# Time: O(n) | Space: O(h) (recursion stack)
# Problem (summary): is there a root-to-LEAF path whose values add up to targetSum?
# Key idea: "going down" = calling the function on a child. Pass down how much is still missing:
# targetSum - root.val (subtract the node you STAND on, not the child's value). At a leaf
# (no left AND no right child) check root.val == targetSum. Answer = left OR right (one path is
# enough; #100 used AND because both sides had to match). Empty tree -> False.
# Mistakes hit: passed nodes (root.left/right) as the number argument; root.val - targetSum
# (wrong sign); leaf check on recursion RESULTS (not left or not right) instead of children
# (not root.left and not root.right); `val` instead of root.val; missing final return.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            if root.val == targetSum:
                return True

        left = self.hasPathSum(root.left, targetSum - root.val)
        right = self.hasPathSum(root.right, targetSum - root.val)

        return left or right


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
    print(Solution().hasPathSum(build([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), 22))  # True
    print(Solution().hasPathSum(build([1, 2, 3]), 5))  # False
    print(Solution().hasPathSum(build([]), 0))  # False
    print(Solution().hasPathSum(build([1, 2]), 1))  # False (1 is not a leaf)
