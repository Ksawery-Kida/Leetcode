# 199. Binary Tree Right Side View — Medium (NeetCode 150)
# https://leetcode.com/problems/binary-tree-right-side-view/
# Pattern: BFS by levels (skeleton from #102)
# Time: O(n) | Space: O(n)
# Problem (summary): looking at the tree from the right, return the visible values top to bottom.
# Key idea: from the right you see exactly ONE node per level — the LAST one on that level
# (it can be a LEFT child if nothing stands to its right, e.g. [1,2,3,4] -> 4). Reuse the #102
# BFS skeleton; the only change: result gets level[-1] instead of the whole level, appended once
# per level (after the for loop, inside while). No sorting — the queue already gives left-to-right.
# Mistakes hit: only followed right children (missed visible left nodes); recursion on the same
# root (infinite); argument count mismatch; "if no right child take the left one" (visibility
# depends on the whole LEVEL, not the parent: [1,2,3,null,5,null,4] -> [1,3,4]); empty deque()
# instead of deque([root]); result.append inside the for loop (every node added).

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Mega mocny problem ale zauwazylem schemat liczenia leveli i moglem go skopiowac z mojego
        # szkieletu #102, na koncu wystarczylo tylko zmienic to zeby nie wszystkie node'y trafialy
        # do result tylko ostatni node z kazdego poziomu (level[-1]), bo patrzac z prawej widac
        # dokladnie jeden node na poziom. Wystarczylo przesunac result.append poza petle for.
        if not root:
            return []

        q = deque([root])
        result = []

        while q:
            size = len(q)
            level = []

            for x in range(size):
                node = q.popleft()

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

                level.append(node.val)
            result.append(level[-1])
        return result


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
    print(Solution().rightSideView(build([1, 2, 3, None, 5, None, 4])))  # [1, 3, 4]
    print(Solution().rightSideView(build([1, 2, 3, 4])))  # [1, 3, 4]
    print(Solution().rightSideView(build([])))  # []
