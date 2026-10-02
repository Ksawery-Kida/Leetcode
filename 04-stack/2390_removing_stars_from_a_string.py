# 2390. Removing Stars From a String — Medium
# https://leetcode.com/problems/removing-stars-from-a-string/
# Pattern: stack (like #844)
# Time: O(n) | Space: O(n)
# Problem (summary): each "*" removes itself and the closest non-star character to its left.
# Return the string after all removals.
# Key idea: ONE loop. "*" -> pop() ONCE (the star itself never goes on the stack),
# letter -> append. Return "".join(stack).

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c == "*":
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)


if __name__ == "__main__":
    print(Solution().removeStars("leet**cod*e"))  # "lecoe"
    print(Solution().removeStars("erase*****"))  # ""
