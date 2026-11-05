# 111. Minimum Depth of Binary Tree — Easy
# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Pattern: tree DFS, depth passed DOWN as an argument + shared self.result list
# Time: O(n) | Space: O(n) (result list) + O(h) (recursion stack)
# Problem (summary): number of NODES on the shortest root-to-LEAF path (empty tree -> 0).
# Key idea (own approach): helper(node, count) — count = depth of the node it stands on (root = 1),
# children get count + 1 in the CALL (doesn't change the parent's count). At a LEAF
# (no left AND no right child) append count to self.result. Answer = min(self.result).
# Gotcha of the problem: the path must end at a leaf — a node with one child is NOT an end.
# Two `if not root` checks with different jobs: in minDepth = empty WHOLE tree (return 0 to
# LeetCode); in the helper = recursion base case.
# Solved MOSTLY ALONE (first problem under the quality-over-quantity rules, 2026-11-05).
# Snags hit: recursion var is fresh in every call (pass it as an argument, not a local count = 0);
# helper params / missing count arg in the first call; self.result(append(...)); no base case
# (NoneType has no .left); depth counted in nodes, root starts at 1; count += 1 AND count + 1
# (added twice) -> only count + 1 in both calls; append at every node -> only at leaves;
# min() of an empty list for [] -> early return 0 in minDepth; IndentationError (mixed indent).

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        # Przyjemny problem, wpadlem na pomysl z lista i countem i uparlem sie zeby uzyc,
        # kombinowalem chwile ale jakos mi sie udalo

        if not root:  # base case CALEJ funkcji
            return 0

        self.result = []
        self.count_helper(root, 1)
        return min(self.result)

    def count_helper(self, root, count):
        if not root:  # base case rekurencji
            return

        self.count_helper(root.left, count + 1)
        self.count_helper(root.right, count + 1)

        if not root.right and not root.left:
            self.result.append(count)


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
    print(Solution().minDepth(build([3, 9, 20, None, None, 15, 7])))  # 2
    print(Solution().minDepth(build([2, None, 3, None, 4, None, 5, None, 6])))  # 5
    print(Solution().minDepth(build([])))  # 0
    print(Solution().minDepth(build([1, 2])))  # 2
