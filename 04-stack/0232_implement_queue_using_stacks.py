# 232. Implement Queue using Stacks — Easy
# https://leetcode.com/problems/implement-queue-using-stacks/
# Pattern: stack (two stacks -> queue)
# Time: push O(1), pop/peek amortized O(1) | Space: O(n)
# Key idea: push -> self.stack (input). pop/peek read from the end of self.stack2 (output).
# Move everything stack -> stack2 ONLY when stack2 is empty (reverses order, oldest lands at the end).
# Moving while stack2 still has items breaks FIFO (push1, push2, pop, push3, pop -> 3 instead of 2).
# Every list stored on the object needs self. in EVERY line — also inside loops and calls.

class MyQueue:

    def __init__(self):
        self.stack = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack:
                self.stack2.append(self.stack.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            while self.stack:
                self.stack2.append(self.stack.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        if not self.stack and not self.stack2:
            return True
        else:
            return False


if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    print(q.peek())   # 1
    print(q.pop())    # 1
    q.push(3)
    print(q.pop())    # 2
    print(q.empty())  # False
