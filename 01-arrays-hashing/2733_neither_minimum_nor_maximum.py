# 2733. Neither Minimum nor Maximum — Easy
# https://leetcode.com/problems/neither-minimum-nor-maximum/
# Pattern: array, built-ins max()/min() + one pass
# Time: O(n) | Space: O(1)
# Problem (summary): return any number that is neither the min nor the max of nums, else -1.
# Key idea: compute max and min once, return the first value that is != both. If the loop ends
# without returning (e.g. only 2 elements) -> -1. Condition needs AND (not max AND not min).
# Solved first try. (O(1) trick: sort the first 3 elements and return the middle one.)

from typing import List


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:

        maximum = max(nums)
        minimum = min(nums)

        for c in nums:
            if c != maximum and c != minimum:
                return c

        return -1


if __name__ == "__main__":
    print(Solution().findNonMinOrMax([3, 2, 1, 4]))  # 2 or 3
    print(Solution().findNonMinOrMax([1, 2]))  # -1
    print(Solution().findNonMinOrMax([2, 1, 3]))  # 2
