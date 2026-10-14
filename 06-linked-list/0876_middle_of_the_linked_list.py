# 876. Middle of the Linked List — Easy
# https://leetcode.com/problems/middle-of-the-linked-list/
# Pattern: linked list, fast & slow pointers
# Time: O(n) | Space: O(1)
# Problem (summary): return the middle node (the second middle if the length is even).
# Key idea: no indexes and no known end. Both start at head; slow = slow.next (1 step),
# fast = fast.next.next (2 steps). Loop while fast and fast.next (otherwise .next.next crashes).
# When fast reaches the end, slow is in the middle.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


def build(values):
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


if __name__ == "__main__":
    print(Solution().middleNode(build([1, 2, 3, 4, 5])).val)  # 3
    print(Solution().middleNode(build([1, 2, 3, 4, 5, 6])).val)  # 4
