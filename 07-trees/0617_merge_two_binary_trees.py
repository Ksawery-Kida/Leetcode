# 617. Merge Two Binary Trees — Easy
# https://leetcode.com/problems/merge-two-binary-trees/
# Pattern: tree, recursive DFS on two trees at once (like #100)
# Time: O(min(n, m)) | Space: O(h) (recursion stack)
# Problem (summary): overlay two trees — where both have a node, sum the values; where only
# one has a node, take that node (with its whole subtree).
# Key idea: no new tree needed — modify root1 in place and return it. Base cases: only root1
# -> return root1, only root2 -> return root2 (the whole branch is "transplanted"). Both exist:
# root1.val += root2.val, recurse on pairs (left, left) / (right, right) and ATTACH the results:
# root1.left = self.mergeTrees(...). The recursion returns a NODE, not a bool.
# Mistakes hit: self.TreeNode(...) instead of self.mergeTrees(...) (creating vs going down);
# 4 calls (each tree separately) instead of 2 paired calls; base cases returned None instead of
# the existing node; added children's .val instead of the current node's; tried
# root1.left + root2.left (can't + nodes); recursion results not attached; missing return.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:  # Checking the base cases
            return None
        if root1 and not root2:
            return root1
        if not root1 and root2:
            return root2

        left = self.mergeTrees(root1.left, root2.left)  # left recursion
        root1.left = left  # merging

        right = self.mergeTrees(root1.right, root2.right)  # right recursion
        root1.right = right  # merging

        root1.val += root2.val  # merging values

        return root1


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


def to_list(root):
    """Tree -> LeetCode level-order list (trailing Nones trimmed)."""
    out, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            out.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            out.append(None)
    while out and out[-1] is None:
        out.pop()
    return out


if __name__ == "__main__":
    print(to_list(Solution().mergeTrees(build([1, 3, 2, 5]), build([2, 1, 3, None, 4, None, 7]))))  # [3, 4, 5, 5, 4, None, 7]
    print(to_list(Solution().mergeTrees(build([1]), build([1, 2]))))  # [2, 2]
    print(to_list(Solution().mergeTrees(build([]), build([]))))  # []
