# 1022. Sum of Root To Leaf Binary Numbers — Easy
# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
# Pattern: tree DFS with a value passed DOWN as an argument (like #257, #1448) + self.outcome
# Time: O(n) | Space: O(h)
# Problem (summary): every node is 0 or 1; each root-to-leaf path is a binary number
# (1->0->1 = 0b101 = 5). Return the sum of all these numbers.
# Key idea: appending a binary digit = shift left + add: new_path = path * 2 + root.val
# (decimal analogy: 12 -> 123 is 12 * 10 + 3). Start with path = 0, pass new_path to both
# children, add it to self.outcome at a leaf. Alternative: build a string and int(path, 2).
# Mistakes hit: helper did not receive the path from the parent (only the leaf digit was
# saved); path + root.val ADDS instead of appending a digit; `def helper` indented inside the
# main method; returned the helper's result (None) instead of self.outcome.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.outcome = 0
        self.helper(root, 0)
        return self.outcome

    def helper(self, root, path):
        if not root:
            return 0

        new_path = path * 2 + root.val

        left = self.helper(root.left, new_path)
        right = self.helper(root.right, new_path)

        if not root.left and not root.right:
            self.outcome += new_path


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
    print(Solution().sumRootToLeaf(build([1, 0, 1, 0, 1, 0, 1])))  # 22
    print(Solution().sumRootToLeaf(build([0])))  # 0
