# 572. Subtree of Another Tree — Easy
# https://leetcode.com/problems/subtree-of-another-tree/
# Pattern: tree, DFS + helper (#100 Same Tree)
# Time: O(n * m) | Space: O(h)
# Problem (summary): does root contain a subtree identical to subRoot?
# Key idea: the problem CONTAINS a problem already solved -> reuse it as a helper.
# At every node: isSameTree(root, subRoot)? -> True. Otherwise subRoot may start in the
# left OR the right subtree -> return left or right. subRoot never changes in the recursion,
# only where we look (root.left / root.right).
# Mistakes hit: called isSubtree with one argument (needs subRoot too); root == subRoot checks
# if it's the SAME OBJECT in memory, not equal-looking trees; compared only the root value
# instead of the whole structure; left/right results ignored.
# Lesson: before coding, ask "have I already solved a piece of this?" (#101 isMirror, #572 isSameTree).

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        if self.isSameTree(root, subRoot):
            return True

        else:
            return right or left

    def isSameTree(self, p, q):
        if not p and not q:
            return True

        if not p and q:
            return False

        if not q and p:
            return False

        if q.val != p.val:
            return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        if left and right:
            return True

        else:
            return False


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
    print(Solution().isSubtree(build([3, 4, 5, 1, 2]), build([4, 1, 2])))  # True
    print(Solution().isSubtree(build([3, 4, 5, 1, 2, None, None, None, None, 0]), build([4, 1, 2])))  # False
    print(Solution().isSubtree(build([1, 1]), build([1])))  # True
