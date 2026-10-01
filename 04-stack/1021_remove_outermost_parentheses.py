# 1021. Remove Outermost Parentheses — Easy
# https://leetcode.com/problems/remove-outermost-parentheses/
# Pattern: stack
# Time: O(n) | Space: O(n)
# Key idea: empty stack = we're at an OUTER bracket. "(": add to result only if stack is
# not empty, then push. ")": pop first, then add to result only if stack is still not empty.
# Every bracket goes on / comes off the stack exactly once.

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        result = []
        for c in s:
            if c == "(":
                if stack:
                    result.append(c)
                stack.append(c)
            else:
                stack.pop()
                if stack:
                    result.append(c)
        return "".join(result)


if __name__ == "__main__":
    print(Solution().removeOuterParentheses("(()())(())"))  # "()()()"
    print(Solution().removeOuterParentheses("(()())(())(()(()))"))  # "()()()()(())"
    print(Solution().removeOuterParentheses("()()"))  # ""
