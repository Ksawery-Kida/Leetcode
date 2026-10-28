# 1290. Convert Binary Number in a Linked List to Integer — Easy
# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
# Pattern: linked list traversal + building a number digit by digit
# Time: O(n) | Space: O(1)
# Problem (summary): the list holds bits (most significant first); return the decimal value.
# Key idea: like "12 -> 123" in decimal (result * 10 + digit), in binary result * 2 + bit.
# Walk from head with `while curr`, update result for EVERY node (0 bits matter too — they
# shift everything left), then move. Start from result = 0, so the first bit needs no special case.
# Mistakes hit: compared curr.val to "0" (string, vals are ints); filtered bits with an if;
# moved before computing (skipped head); `while curr and curr.next` (skipped the last node);
# unneeded prev / first-node special case — overcomplicated after trees and base cases.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        curr, result = head, 0

        while curr:
            result = result * 2 + curr.val
            curr = curr.next

        return result


def build(values):
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


if __name__ == "__main__":
    print(Solution().getDecimalValue(build([1, 0, 1])))  # 5
    print(Solution().getDecimalValue(build([0])))  # 0
    print(Solution().getDecimalValue(build([1, 1, 0])))  # 6
