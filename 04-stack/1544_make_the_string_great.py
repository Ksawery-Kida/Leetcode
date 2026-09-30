# 1544. Make The String Great — Easy
# https://leetcode.com/problems/make-the-string-great/
# Pattern: stack (like #1047)
# Time: O(n) | Space: O(n)
# Key idea: pop when c and stack[-1] are the same letter in different case:
# stack and c != stack[-1] and c.lower() == stack[-1].lower(). Else append. Return "".join(stack).

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and c != stack[-1] and c.lower() == stack[-1].lower():
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)


if __name__ == "__main__":
    print(Solution().makeGood("leEeetcode"))  # "leetcode"
    print(Solution().makeGood("abBAcC"))  # ""
    print(Solution().makeGood("s"))  # "s"
