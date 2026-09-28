# 150. Evaluate Reverse Polish Notation — Medium
# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Pattern: stack
# Time: O(n) | Space: O(n)
# Key idea: number -> append int(c). Operator -> pop the last two numbers, append the result.
# Compare with c == "-" (not "-" in c), otherwise "-11" is treated as minus.
# Division: int(a / b) truncates toward zero, // rounds down (wrong for negatives).

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for c in tokens:
            if c == "-":
                stack.append(stack.pop(-2) - stack.pop(-1))
            elif c == "+":
                stack.append(stack.pop(-2) + stack.pop(-1))
            elif c == "*":
                stack.append(stack.pop(-2) * stack.pop(-1))
            elif c == "/":
                stack.append(int(stack.pop(-2) / stack.pop(-1)))
            else:
                stack.append(int(c))
        return stack[-1]


if __name__ == "__main__":
    print(Solution().evalRPN(["2", "1", "+", "3", "*"]))  # 9
    print(Solution().evalRPN(["4", "13", "5", "/", "+"]))  # 6
    print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))  # 22
