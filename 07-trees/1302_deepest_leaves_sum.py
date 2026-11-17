# 1302. Deepest Leaves Sum — Medium
# https://leetcode.com/problems/deepest-leaves-sum/
# Pattern: BFS by level (same skeleton as #102, #637)
# Time: O(n) | Space: O(w) (w = max width of a level)
# Problem (summary): return the sum of the values of the leaves on the deepest level.
# Key idea: `level = []` is reset at the start of every while-iteration, so after the loop
# ends `level` still holds the LAST (deepest) level -> return sum(level).
# Mistakes hit: first summed ALL leaves (a leaf can sit on a shallower level, e.g. node 5 in
# [1,2,3,4,5,null,6,7,null,null,null,null,8] -> 20 instead of 15); deque(root) instead of
# deque([root]); popleft without (); level.append only inside `if node.right`.
# Note: `result` is not needed — sum(level) alone gives the answer.

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

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
            result.append(level)

        return sum(level)


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
    print(Solution().deepestLeavesSum(build([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8])))  # 15
    print(Solution().deepestLeavesSum(build([6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5])))  # 19
