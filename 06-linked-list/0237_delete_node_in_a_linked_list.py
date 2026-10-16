# 237. Delete Node in a Linked List — Medium (feels Easy)
# https://leetcode.com/problems/delete-node-in-a-linked-list/
# Pattern: linked list, overwrite value + skip
# Time: O(1) | Space: O(1)
# Problem (summary): given only the node to delete (no head, never the tail), remove it in place.
# Key idea: we can't reach the previous node, so we can't re-point its arrow. Instead copy the
# next node's value into this one (4 -> 5 -> 1 -> 9 becomes 4 -> 1 -> 1 -> 9), then skip the
# next node (-> 4 -> 1 -> 9). No loop, no if. Gotcha: `node = node.next` only moves the local
# variable — the list doesn't change; you need `.val` on both sides.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


def build(values):
    head = None
    for v in reversed(values):
        node = ListNode(v)
        node.next = head
        head = node
    return head


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    head = build([4, 5, 1, 9])
    Solution().deleteNode(head.next)  # delete 5
    print(to_list(head))  # [4, 1, 9]

    head = build([4, 5, 1, 9])
    Solution().deleteNode(head.next.next)  # delete 1
    print(to_list(head))  # [4, 5, 9]
