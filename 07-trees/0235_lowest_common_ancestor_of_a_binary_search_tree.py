# 235. Lowest Common Ancestor of a Binary Search Tree — Medium (NeetCode 150)
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Pattern: BST, recursive search going ONE way (same shape as #700)
# Time: O(h) | Space: O(h) (recursion stack)
# Problem (summary): return the lowest node that has both p and q as descendants
# (a node counts as its own descendant).
# Key idea: compare BOTH p.val and q.val with root.val. Both smaller -> LCA is in the left
# subtree; both bigger -> right subtree; otherwise (they split, or one of them IS root) ->
# root is the answer (going lower would lose one of them). Return the recursion result directly.
# Mistakes hit: thought the "split" case means discarding — it's actually the answer;
# base case returned 0 instead of None; calls missing p, q args; results stored in left/right
# instead of returned; "both bigger" condition compared q the wrong way; redundant elif before else.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)

        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)

        else:
            return root


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


def find(root, val):
    while root and root.val != val:
        root = root.left if val < root.val else root.right
    return root


if __name__ == "__main__":
    t = build([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    print(Solution().lowestCommonAncestor(t, find(t, 2), find(t, 8)).val)  # 6
    print(Solution().lowestCommonAncestor(t, find(t, 2), find(t, 4)).val)  # 2
    print(Solution().lowestCommonAncestor(t, find(t, 3), find(t, 5)).val)  # 4
