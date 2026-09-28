# 682. Baseball Game — Easy
# https://leetcode.com/problems/baseball-game/
# Pattern: stack
# Time: O(n) | Space: O(n)
# Key idea: stack holds valid scores. "C" -> pop, "D" -> append 2 * stack[-1],
# "+" -> append stack[-1] + stack[-2], number -> append int(op). Answer = sum(stack).

class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []
        for op in operations:
            if op == "C":
                stack.pop()
            elif op == "D":
                stack.append(2 * stack[-1])
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))
        return sum(stack)


if __name__ == "__main__":
    print(Solution().calPoints(["5", "2", "C", "D", "+"]))  # 30
    print(Solution().calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))  # 27
    print(Solution().calPoints(["1", "C"]))  # 0
