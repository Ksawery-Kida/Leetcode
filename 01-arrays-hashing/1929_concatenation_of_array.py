# 1929. Concatenation of Array — Easy
# https://leetcode.com/problems/concatenation-of-array/
# Pattern: none (language tool: list + list)
# Time: O(n) | Space: O(n)
# Key idea: + on lists glues them together (nums * 2 works too).

class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums + nums


if __name__ == "__main__":
    print(Solution().getConcatenation([1, 2, 1]))  # [1, 2, 1, 1, 2, 1]
    print(Solution().getConcatenation([1, 3, 2, 1]))  # [1, 3, 2, 1, 1, 3, 2, 1]
