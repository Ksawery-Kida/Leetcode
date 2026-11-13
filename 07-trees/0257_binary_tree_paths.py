# 257. Binary Tree Paths — Easy
# https://leetcode.com/problems/binary-tree-paths/
# Pattern: tree DFS with a value (path string) passed DOWN as an argument (like #1448) + self.result
# Time: O(n * h) (string building) | Space: O(n * h)
# Problem (summary): return every root-to-leaf path as a string "1->2->5".
# Key idea: each call gets the path from its parent, builds new_path by gluing its own value on
# (no arrow when path is still empty), passes new_path to BOTH children, and appends new_path
# when it is a leaf. Every call has its own copy of the string, so branches do not mix.
# Mistakes hit: base case read root.val on None; shared self.path idea (branches would mix);
# overwrote the parent's path with str(root.val) (history lost -> "5->5"); passed the old path
# to the children instead of new_path; start value str(root.val) duplicated the root;
# variable name with a space (new path).

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> list[str]:
        self.result = []
        self.helper(root, "")
        return self.result

    def helper(self, root, path):
        if not root:
            return []

        if path == "":
            new_path = str(root.val)
        else:
            new_path = path + "->" + str(root.val)

        left = self.helper(root.left, new_path)
        right = self.helper(root.right, new_path)

        if not root.left and not root.right:
            self.result.append(new_path)


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
    print(Solution().binaryTreePaths(build([1, 2, 3, None, 5])))  # ['1->2->5', '1->3']
    print(Solution().binaryTreePaths(build([1])))  # ['1']
