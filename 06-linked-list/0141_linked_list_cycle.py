# 141. Linked List Cycle — Easy
# https://leetcode.com/problems/linked-list-cycle/
# Pattern: linked list, fast & slow pointers (Floyd)
# Time: O(n) | Space: O(1)
# Problem (summary): does the list loop back on itself?
# Key idea: same as #876, but if there is a cycle, fast (2 steps) eventually laps slow (1 step)
# and they meet -> True. If fast reaches None -> no cycle -> False.
# Bug to avoid: fast = fast.next (1 step) -> both move together -> always True.
# Redo 2026-10-20: same 1-step bug again + `else: return False` inside the loop (exits after the
# first iteration) — return False belongs AFTER the loop; loop condition is fast and fast.next.

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False


if __name__ == "__main__":
    nodes = [ListNode(v) for v in [3, 2, 0, -4]]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    print(Solution().hasCycle(nodes[0]))  # False
    nodes[-1].next = nodes[1]
    print(Solution().hasCycle(nodes[0]))  # True
