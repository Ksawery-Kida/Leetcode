# 94. Binary Tree Inorder Traversal — Easy
# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Pattern: tree DFS (inorder) + helper that fills a shared list
# Time: O(n) | Space: O(n) (result) + O(h) (recursion stack)
# Problem (summary): return node values in inorder: left subtree -> node -> right subtree.
# Key idea: the result list must be created ONCE, outside the recursion (result = [] inside a
# recursive function makes a new empty list on every call). So: main creates self.result, calls
# the helper on root, returns self.result. Helper: base case (bare return) -> left -> append(root.val)
# -> right. Each call appends only the node it STANDS on; children append themselves in their own
# calls. Position of append = order: before both = preorder, between = inorder, after = postorder.
# self.result (not result) so both methods see the same list. Alternative: pass the list as an arg.
# Mistakes hit: self.result = [] inside the recursive function; appended root.left.val/root.right.val
# instead of root.val; 2 args to a 1-node function; result without self.; helper/main roles swapped
# (helper created the list, helper called the main function); def calling() without self/root;
# return self.calling(root) -> returns None (helper returns nothing) — call it, then return the list.
# Approach felt illogical -> REDO several times (also list-as-argument version, pre/postorder).

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []  # zapisuje ogolna liste
        self.calling(root)  # wywoluje calling - zbieram wartosci node'ow
        return self.result  # zwracam wynik

    def calling(self, root):

        if not root:  # base case
            return

        self.calling(root.left)  # rekurencja po lewej
        self.result.append(root.val)  # dodawanie do ogolnej listy
        self.calling(root.right)  # rekurencja do prawej


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
    print(Solution().inorderTraversal(build([1, None, 2, 3])))  # [1, 3, 2]
    print(Solution().inorderTraversal(build([4, 2, 6, 1, 3, 5, 7])))  # [1, 2, 3, 4, 5, 6, 7]
    print(Solution().inorderTraversal(build([])))  # []
