# 1047. Remove All Adjacent Duplicates In String — Easy
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
# Pattern: stack
# Time: O(n) | Space: O(n)
# Key idea: if c equals the last element of the stack -> pop (they cancel out),
# otherwise append c. At the end "".join(stack) turns the list back into a string.

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)


if __name__ == "__main__":
    print(Solution().removeDuplicates("abbaca"))  # "ca"
    print(Solution().removeDuplicates("azxxzy"))  # "ay"
    print(Solution().removeDuplicates("aa"))  # ""
