# 155. Min Stack — Medium
# https://leetcode.com/problems/min-stack/
# Pattern: stack (two stacks)
# Time: O(1) per operation | Space: O(n)
# Key idea: min_stack stores the current minimum for every push, so it has the same
# length as stack. push -> append min(value, min_stack[-1]); pop -> pop both;
# getMin -> min_stack[-1].

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.min_stack:
            self.min_stack.append(value)
        else:
            x = min(value, self.min_stack[-1])
            self.min_stack.append(x)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


if __name__ == "__main__":
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    print(s.getMin())  # -3
    s.pop()
    print(s.top())  # 0
    print(s.getMin())  # -2
