# 872. Leaf-Similar Trees — Easy
# https://leetcode.com/problems/leaf-similar-trees/
# Pattern: tree DFS collecting leaf values into a shared self list (one helper call per tree)
# Time: O(n + m) | Space: O(n + m)
# Problem (summary): two trees are leaf-similar if their leaf values, read left to right, form
# the same sequence.
# Key idea: DFS each tree separately (left child before right keeps the left-to-right order),
# append a node's value only when it has no children, then compare the two lists.
# Mistakes hit: one helper walking both trees at once (values of the two trees got mixed);
# recursive calls with two children as "root1, root2"; missing base case (None.left crash);
# no return for the "lists differ" case (returned None instead of False).

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Bardzo przyjemne zadanie. Chwile sie glowilem, bo na poczatku chcialem wywolac
        # rekurencje dla obu drzew w jednej funkcji i wtedy mieszaly mi sie values obu drzew,
        # ale szybko to rozwiklalem. Napewno wroce do tego zadania czasem na rozgrzewke.

        # base cases
        if not root1 or not root2:
            return False
        if not root1 and root2:
            return False
        if root1 and not root2:
            return False

        self.result_root1 = []
        self.result_root2 = []
        self.leaf_counter_1(root1)
        self.leaf_counter_2(root2)

        if self.result_root1 == self.result_root2:
            return True
        else:
            return False

    def leaf_counter_1(self, root1):
        if not root1:
            return False

        self.leaf_counter_1(root1.left)
        self.leaf_counter_1(root1.right)

        # warunek na append
        if not root1.left and not root1.right:
            self.result_root1.append(root1.val)

    def leaf_counter_2(self, root2):
        if not root2:
            return False

        self.leaf_counter_2(root2.left)
        self.leaf_counter_2(root2.right)

        # warunek na append
        if not root2.left and not root2.right:
            self.result_root2.append(root2.val)


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
    print(Solution().leafSimilar(
        build([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]),
        build([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8])))  # True
    print(Solution().leafSimilar(build([1, 2, 3]), build([1, 3, 2])))  # False
    print(Solution().leafSimilar(build([1]), build([1])))  # True
