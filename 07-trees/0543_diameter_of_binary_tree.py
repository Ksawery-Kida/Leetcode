# 543. Diameter of Binary Tree — Easy (NeetCode 150)
# https://leetcode.com/problems/diameter-of-binary-tree/
# Pattern: tree DFS, helper that RETURNS one thing (height) and UPDATES another (self.maximum)
# Time: O(n) | Space: O(h) (recursion stack)
# Problem (summary): length (in EDGES) of the longest path between any two nodes; the path does
# not have to go through the root.
# Key idea: at every node the longest path that "bends" there = height(left) + height(right)
# (heights counted in nodes as in #104, each node down one side = one edge). Keep the best in
# self.maximum = max(self.maximum, left + right). The helper must still RETURN its height to the
# parent: 1 + max(left, right). Main: self.maximum = 0, call helper on root, return self.maximum.
# Mistakes hit: return self.count1 = self.count2 (assignment in return); helper called the main
# function (resets the counter, same as #94); self.count += 1 counted visits, not height (same as
# #110); compared left vs right instead of adding; left + right - 1; self.max (max is built-in);
# helper returned nothing / max(left, right) without +1; extra unused `count` param;
# two variables mixed (self.count never updated, self.maximum never initialized).
# Heavily guided -> in the Redo queue.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.maximum = 0
        self.counting_nodes(root)
        return self.maximum

    def counting_nodes(self, root):
        if not root:
            return 0

        left = self.counting_nodes(root.left)
        right = self.counting_nodes(root.right)

        self.maximum = max(self.maximum, (left + right))

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
    print(Solution().diameterOfBinaryTree(build([1, 2, 3, 4, 5])))  # 3
    print(Solution().diameterOfBinaryTree(build([1, 2])))  # 1
    print(Solution().diameterOfBinaryTree(build([1, 2, None, 3, 4, 5, None, None, 6])))  # 4 (not through root)
