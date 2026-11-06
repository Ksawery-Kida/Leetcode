# 1448. Count Good Nodes in Binary Tree — Medium (NeetCode 150)
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Pattern: tree DFS, value passed DOWN as an argument (same scheme as #111) + shared self.result
# Time: O(n) | Space: O(h)
# Problem (summary): a node is good if no node on the path root -> node has a GREATER value;
# count the good nodes (the root is always good).
# Key idea: the only thing you need from the path above is its MAXIMUM. Pass it down: update
# count = max(count, root.val) BEFORE both recursive calls so both children get the new max.
# Node is good if the path max does not exceed its value. Start with root.val — the path to the
# root contains only the root; a made-up start (1, 0) acts like an invisible node above the root
# and breaks on negative values.
# Mistakes hit: "seen" set idea (membership says nothing about bigger values; global set mixes
# branches); compared only with the parent (3 -> 1 -> 2: 2 > 1 but 3 is above); compared int with
# a node (root instead of root.val); passed count unchanged (every node counted); max update
# between / after the calls (children got the old max); start value 1 / 0 with negative values.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        # Ciekawy problem ale dosc schematyczny, rozwiazywalem wczoraj #111 i zauwazylem ze da sie
        # tutaj zastosowac ten sam schemat z przekazywaniem argumentu wiec go uzylem. Jedyne z czym
        # sie glowilem to ze chcialem startowac z 1, co bylo bez sensu, bo sciezka do korzenia
        # zawiera tylko sam korzen, wiec jej maksimum to root.val. Zmyslona liczba na starcie dziala
        # jak niewidzialny node nad korzeniem i przy ujemnych wartosciach blokuje korzen.

        if not root:
            return 0

        self.result = 0
        self.counter(root, root.val)
        return self.result

    def counter(self, root, count):
        if not root:
            return

        count = max(count, root.val)

        self.counter(root.right, count)
        self.counter(root.left, count)

        if max(count, root.val) <= root.val:
            self.result += 1


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
    print(Solution().goodNodes(build([3, 1, 4, 3, None, 1, 5])))  # 4
    print(Solution().goodNodes(build([3, 3, None, 4, 2])))  # 3
    print(Solution().goodNodes(build([1])))  # 1
    print(Solution().goodNodes(build([-1, -2, -3])))  # 1 (negative values)
