# 637. Average of Levels in Binary Tree — Easy
# https://leetcode.com/problems/average-of-levels-in-binary-tree/
# Pattern: BFS level by level (same skeleton as #102 / #199)
# Time: O(n) | Space: O(w), w = max width of a level
# Problem (summary): return the average value of the nodes on each level.
# Key idea: take size = len(q) at the start of each level, collect that level's values,
# append sum(level) / len(level).
# Mistakes hit: divided by 2 instead of the level size (root level has 1 node -> 1.5 instead of 3).

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> list[float]:
        if not root:
            return []

        q = deque([root])
        result = []

        while q:
            size = len(q)
            level = []

            for x in range(size):
                node = q.popleft()

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

                level.append(node.val)
            result.append(sum(level) / len(level))

        return result


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
    print(Solution().averageOfLevels(build([3, 9, 20, None, None, 15, 7])))  # [3.0, 14.5, 11.0]
    print(Solution().averageOfLevels(build([3, 9, 20, 15, 7])))  # [3.0, 14.5, 11.0]
    print(Solution().averageOfLevels(build([1])))  # [1.0]
