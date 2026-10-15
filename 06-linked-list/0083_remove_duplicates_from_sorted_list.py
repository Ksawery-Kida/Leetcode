# 83. Remove Duplicates from Sorted List — Easy
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Pattern: linked list, single pointer + skipping a node
# Time: O(n) | Space: O(1)
# Problem (summary): sorted linked list -> remove repeated values, return head.
# Key idea: sorted -> duplicates are neighbours. If curr.val == curr.next.val:
# curr.next = curr.next.next (arrow skips the duplicate, curr stays); else curr = curr.next.
# Return head (curr ends at the tail). A stack would need rebuilding a new linked list -> not worth it.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


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
    print(to_list(Solution().deleteDuplicates(build([1, 1, 2]))))  # [1, 2]
    print(to_list(Solution().deleteDuplicates(build([1, 1, 2, 3, 3]))))  # [1, 2, 3]
    print(to_list(Solution().deleteDuplicates(build([1, 1, 1]))))  # [1]
