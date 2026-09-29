# 20. Valid Parentheses — Easy
# https://leetcode.com/problems/valid-parentheses/
# Pattern: stack
# Time: O(n) | Space: O(n)
# Key idea: opening bracket -> append to stack. Closing bracket -> pop the last opening
# and check it matches via close_to_open. At the end the stack must be empty.

class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in s:
            if c not in close_to_open:
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if close_to_open[c] != top:
                    return False
        if stack:
            return False
        else:
            return True


# Redo 2026-09-29 (from scratch, alone): peek with stack[-1], pop only on match.
class SolutionPeek:
    def isValid(self, s: str) -> bool:
        close_to_open = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in s:
            if c not in close_to_open:
                stack.append(c)
            else:
                if not stack:
                    return False
                a = stack[-1]
                if a == close_to_open[c]:
                    stack.pop()
                else:
                    return False
        return not stack


if __name__ == "__main__":
    print(Solution().isValid("()"))      # True
    print(Solution().isValid("()[]{}"))  # True
    print(Solution().isValid("(]"))      # False
    print(Solution().isValid("([])"))    # True
    print(Solution().isValid("((("))     # False
    print(Solution().isValid(")"))       # False
    print(SolutionPeek().isValid("([])"), SolutionPeek().isValid("(]"))  # True False
