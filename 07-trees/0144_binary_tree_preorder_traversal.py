# 144. Binary Tree Preorder Traversal — Easy
# https://leetcode.com/problems/binary-tree-preorder-traversal/
# Pattern: tree DFS + shared self.result (same scheme as #94 inorder)
# Time: O(n) | Space: O(n)
# Problem (summary): return node values in preorder: node, then left subtree, then right subtree.
# Key idea: the only difference between preorder / inorder / postorder is WHERE the append sits
# relative to the two recursive calls. Preorder = append BEFORE both calls.
# Mistakes hit: append between the calls (that is inorder, gave [3,2,1] instead of [2,3,1]).

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        # Trywialne

        self.result = []
        self.helper(root)
        return self.result

    def helper(self, root):
        if not root:
            return []

        self.result.append(root.val)

        left = self.helper(root.left)

        right = self.helper(root.right)


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
    print(Solution().preorderTraversal(build([1, None, 2, 3])))  # [1, 2, 3]
    print(Solution().preorderTraversal(build([2, 3, 1])))  # [2, 3, 1]
    print(Solution().preorderTraversal(build([])))  # []
