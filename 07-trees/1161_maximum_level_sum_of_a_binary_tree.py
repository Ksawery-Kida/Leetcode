# 1161. Maximum Level Sum of a Binary Tree — Medium
# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
# Pattern: BFS by level (same skeleton as #102, #637, #1302) + tracking the best (like #485)
# Time: O(n) | Space: O(w)
# Problem (summary): levels are numbered 1, 2, 3, ...; return the SMALLEST level number
# whose sum of values is the largest.
# Key idea: after each level is collected, level_num += 1 and compare sum(level) with best;
# on a strictly bigger sum remember both the sum (best) and the level number (best_level).
# best starts at -inf because values (and sums) can be negative; `>` (not `>=`) keeps the
# smallest level on ties.
# Mistakes hit: min(level) instead of sum(level); returned the list instead of a level number;
# used one variable `best` as counter, best sum and level list at once; level_num reset inside
# the while / incremented inside the for (counted nodes, not levels); deque[(root)], pop.left().
# Note: `result` is not needed.

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([root])
        result = []

        best = float('-inf')
        level_num, best_level = 0, 0

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

            level_num += 1
            if sum(level) > best:
                best = sum(level)
                best_level = level_num

        return best_level


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
    print(Solution().maxLevelSum(build([1, 7, 0, 7, -8, None, None])))  # 2
    print(Solution().maxLevelSum(build([989, None, 10250, 98693, -89388, None, None, None, -32127])))  # 2
