# 145. Binary Tree Postorder Traversal — Easy
# https://leetcode.com/problems/binary-tree-postorder-traversal/
# Pattern: tree DFS + shared self.result (same scheme as #94 inorder, #144 preorder)
# Time: O(n) | Space: O(n)
# Problem (summary): return node values in postorder: left subtree, right subtree, then node.
# Key idea: postorder = append AFTER both recursive calls.
#   preorder  (#144): append, left, right
#   inorder   (#94):  left, append, right
#   postorder (#145): left, right, append
# Mistakes hit: base case in the main function instead of the helper (None.left crash);
# return self.result inside the helper (main function returned None); append between the calls.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        self.result = []
        self.helper(root)
        return self.result

    def helper(self, root):
        # base cases:
        if not root:
            return []

        left = self.helper(root.left)

        right = self.helper(root.right)
        self.result.append(root.val)


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
    print(Solution().postorderTraversal(build([1, None, 2, 3])))  # [3, 2, 1]
    print(Solution().postorderTraversal(build([2, 3, 1])))  # [3, 1, 2]
    print(Solution().postorderTraversal(build([])))  # []
