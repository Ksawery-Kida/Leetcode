# 2696. Minimum String Length After Removing Substrings — Easy
# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/
# Pattern: stack (like #1047)
# Time: O(n) | Space: O(n)
# Problem (summary): keep removing "AB" and "CD" from s; return the final length.
# Key idea: append each letter, then if len(stack) >= 2 and the last two are "A","B" or "C","D",
# pop both. stack[-1] = last, stack[-2] = second to last (minus = count from the end).

class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for c in s:
            stack.append(c)
            if len(stack) >= 2:
                if stack[-2] == "A" and stack[-1] == "B":
                    stack.pop()
                    stack.pop()
                elif stack[-2] == "C" and stack[-1] == "D":
                    stack.pop()
                    stack.pop()
        return len(stack)


if __name__ == "__main__":
    print(Solution().minLength("ABFCACDB"))  # 2
    print(Solution().minLength("ACBBD"))  # 5
    print(Solution().minLength("ACDB"))  # 0
