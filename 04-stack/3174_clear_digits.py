# 3174. Clear Digits — Easy
# https://leetcode.com/problems/clear-digits/
# Pattern: stack (same as #2390, digit instead of '*')
# Time: O(n) | Space: O(n)
# Key idea: c.isdigit() detects a digit. Solved solo: append every char; if it's a digit, pop twice
# (removes the digit itself, then the closest non-digit on its left). pop(-1) == pop().

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for c in s:
            stack.append(c)
            if c.isdigit():
                stack.pop()
                stack.pop(-1)
        return "".join(stack)


if __name__ == "__main__":
    print(Solution().clearDigits("abc"))   # abc
    print(Solution().clearDigits("cb34"))  # (empty)
