# 234. Palindrome Linked List — Easy
# https://leetcode.com/problems/palindrome-linked-list/
# Pattern: linked list, fast & slow + reverse second half
# Time: O(n) | Space: O(1)
# Problem (summary): does the list read the same forwards and backwards?
# Key idea: combine #876 + #206. (1) fast/slow -> slw ends in the middle. (2) reverse from slw
# to the end (prev/curr/nxt) -> prev = head of the reversed second half. (3) walk left = head
# and prev together comparing .val; any difference -> False, loop finishes -> True.
# No need to split the list — head and prev are two separate starting points.
# Gotchas hit: curr = slw must be set AFTER the fast/slow loop; `nxt = prev` only moves the
# variable, the arrow changes via curr.next = prev (nxt is a copy of where curr.next pointed,
# not an alias); compare .val, not nodes; return True only after the loop.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fst, slw = head, head
        prev = None

        while fst and fst.next:
            fst = fst.next.next
            slw = slw.next

        curr = slw

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        left = head

        while prev:
            if left.val != prev.val:
                return False
            else:
                left = left.next
                prev = prev.next
        return True


def build(values):
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


if __name__ == "__main__":
    print(Solution().isPalindrome(build([1, 2, 2, 1])))  # True
    print(Solution().isPalindrome(build([1, 2])))  # False
    print(Solution().isPalindrome(build([1, 2, 3, 2, 1])))  # True
    print(Solution().isPalindrome(build([1])))  # True
