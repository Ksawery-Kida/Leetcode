# 203. Remove Linked List Elements — Easy
# https://leetcode.com/problems/remove-linked-list-elements/
# Pattern: linked list, single pointer + skipping a node
# Time: O(n) | Space: O(1)
# Problem (summary): remove every node whose value equals val, return the new head.
# Key idea: same skip as #83 but compare curr.next.val with the argument val (not with
# previous nodes). Middle nodes: curr.next = curr.next.next, else curr = curr.next.
# The head itself is never checked by that loop -> before it, `while head and head.val == val:
# head = head.next` (while, not if: e.g. 7 -> 7 -> 7 must become empty).

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        curr = head
        while curr and curr.next:
            if curr.next.val == val:
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
    print(to_list(Solution().removeElements(build([1, 2, 6, 3, 4, 5, 6]), 6)))  # [1, 2, 3, 4, 5]
    print(to_list(Solution().removeElements(build([]), 1)))  # []
    print(to_list(Solution().removeElements(build([7, 7, 7, 7]), 7)))  # []
    print(to_list(Solution().removeElements(build([7, 1, 7]), 7)))  # [1]
