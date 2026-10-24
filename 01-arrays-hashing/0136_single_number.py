# 136. Single Number — Easy
# https://leetcode.com/problems/single-number/
# Pattern: hashing (frequency counter, dict)
# Time: O(n) | Space: O(n)
# Key idea: count every number, then return the one with count 1.
# Bonus (O(1) space): XOR all numbers, pairs cancel out (a ^ a = 0).

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        seen = {}
        for x in nums:
            if x in seen:
                seen[x] += 1
            else:
                seen[x] = 1
        for x in seen:
            if seen[x] == 1:
                return x


if __name__ == "__main__":
    print(Solution().singleNumber([2, 2, 1]))  # 1
    print(Solution().singleNumber([4, 1, 2, 1, 2]))  # 4
    print(Solution().singleNumber([1]))  # 1

# Redo 2026-10-24: re-solved solo.
