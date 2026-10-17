# 100. Same Tree — Easy
# https://leetcode.com/problems/same-tree/
# Pattern: tree, recursive DFS on two trees at once
# Time: O(n) | Space: O(h) (recursion stack)
# Problem (summary): are trees p and q structurally identical with the same values?
# Key idea: no splitting needed — the function takes both trees, so recurse on pairs:
# (p.left, q.left) and (p.right, q.right). Base cases first: both None -> True (two empty trees
# are the same), only one None -> False, different val -> False. Then same iff left AND right.
# Gotchas hit: `none in p` is not how you check existence (use `not p`); val is a node field
# (p.val), not self.val(p); `left == right` is wrong (False == False -> True), need `left and right`.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
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
    """Build a tree from LeetCode level-order list, e.g. [1, 2, 3]."""
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
    print(Solution().isSameTree(build([1, 2, 3]), build([1, 2, 3])))  # True
    print(Solution().isSameTree(build([1, 2]), build([1, None, 2])))  # False
    print(Solution().isSameTree(build([1, 2, 1]), build([1, 1, 2])))  # False
