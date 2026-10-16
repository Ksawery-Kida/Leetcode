# 21. Merge Two Sorted Lists — Easy
# https://leetcode.com/problems/merge-two-sorted-lists/
# Pattern: linked list, dummy node + tail, two pointers
# Time: O(n + m) | Space: O(1)
# Problem (summary): merge two sorted linked lists into one sorted list, return its head.
# Key idea: dummy = ListNode() as a fake start (we don't know the first node yet), tail = dummy.
# One loop `while list1 and list2`: attach the smaller head to tail.next, move THAT list forward,
# then tail = tail.next. After the loop (not inside it!) one list is None -> attach the other
# one's leftover with a single tail.next = ... (it's already linked). Return dummy.next.
# Gotcha: leftover if/else inside the loop broke list1=[], list2=[0] (loop never runs).

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        return dummy.next


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
    print(to_list(Solution().mergeTwoLists(build([1, 2, 4]), build([1, 3, 4]))))  # [1, 1, 2, 3, 4, 4]
    print(to_list(Solution().mergeTwoLists(build([]), build([]))))  # []
    print(to_list(Solution().mergeTwoLists(build([]), build([0]))))  # [0]
    print(to_list(Solution().mergeTwoLists(build([1, 2]), build([3, 4, 5]))))  # [1, 2, 3, 4, 5]
