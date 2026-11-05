# 102. Binary Tree Level Order Traversal — Medium (NeetCode 150)
# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Pattern: BFS with a queue (collections.deque), one level per round
# Time: O(n) | Space: O(n)
# Problem (summary): return node values level by level, left to right, as a list of lists.
# Key idea: BFS = no recursion, a while loop over a queue. Start with deque([root]). Each round:
# size = len(q) taken at the START of the round (= exactly one full level, before children are
# added), new `level` list, then size times: node = q.popleft(), level.append(node.val), append
# existing children to the back. After the for loop (still inside while) result.append(level).
# Queue holds NODES (you need .left/.right later), not values.
# Mistakes hit: returned 0 for empty tree (needs []); mixed in recursion (self.levelOrder) — that's
# DFS; appended values / root.left.val to the queue; deque(0) / deque(root) / deque[root] instead
# of deque([root]); for x in size (needs range(size)); recreated the queue inside the loop;
# popleft() result thrown away; appended the counter x; q.append(a, b) (append takes one item);
# level never added to result; return outside the function.

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
            result.append(level)

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
    print(Solution().levelOrder(build([3, 9, 20, None, None, 15, 7])))  # [[3], [9, 20], [15, 7]]
    print(Solution().levelOrder(build([1])))  # [[1]]
    print(Solution().levelOrder(build([])))  # []
