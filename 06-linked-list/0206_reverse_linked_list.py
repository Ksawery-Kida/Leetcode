# 206. Reverse Linked List — Easy
# https://leetcode.com/problems/reverse-linked-list/
# Pattern: linked list, iterative pointer reversal (prev / curr / nxt)
# Time: O(n) | Space: O(1)
# Problem (summary): reverse a singly linked list, return the new head.
# Key idea: nodes stay in place; only the .next arrows flip and the labels move.
# Each step: nxt = curr.next (remember the rest), curr.next = prev (flip arrow),
# prev = curr, curr = nxt (move right). When curr is None, prev is the new head.
# curr = current, prev = previous, nxt (not "next", which is a Python built-in).

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


def build(values):
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    print(to_list(Solution().reverseList(build([1, 2, 3, 4, 5]))))  # [5, 4, 3, 2, 1]
    print(to_list(Solution().reverseList(build([1, 2]))))  # [2, 1]
    print(to_list(Solution().reverseList(build([]))))  # []
