# 844. Backspace String Compare — Easy
# https://leetcode.com/problems/backspace-string-compare/
# Pattern: stack
# Time: O(n + m) | Space: O(n + m)
# Key idea: helper build() turns a string into its final text: letter -> append,
# "#" -> pop (only if stack not empty). Then compare build(s) == build(t).

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(string):
            stack = []
            for c in string:
                if c == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
            return stack
        return build(s) == build(t)


if __name__ == "__main__":
    print(Solution().backspaceCompare("ab#c", "ad#c"))  # True
    print(Solution().backspaceCompare("ab##", "c#d#"))  # True
    print(Solution().backspaceCompare("a#c", "b"))  # False
