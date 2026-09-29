# 1614. Maximum Nesting Depth of the Parentheses — Easy
# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
# Pattern: stack (as a counter)
# Time: O(n) | Space: O(1)
# Key idea: depth = how many "(" are currently open (= stack length). "(" -> depth += 1 and
# update result = max seen; ")" -> depth -= 1; other chars ignored.

class Solution:
    def maxDepth(self, s: str) -> int:
        result = 0
        depth = 0
        for c in s:
            if c == "(":
                depth += 1
                if depth >= result:
                    result = depth
            elif c == ")":
                depth -= 1
        return result


if __name__ == "__main__":
    print(Solution().maxDepth("(1+(2*3)+((8)/4))+1"))  # 3
    print(Solution().maxDepth("(1)+((2))+(((3)))"))  # 3
    print(Solution().maxDepth("()(())((()()))"))  # 3
    print(Solution().maxDepth("1"))  # 0
