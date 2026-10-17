# 1913. Maximum Product Difference Between Two Pairs — Easy
# https://leetcode.com/problems/maximum-product-difference-between-two-pairs/
# Pattern: array, sorting
# Time: O(n log n) | Space: O(1) (in-place sort)
# Problem (summary): pick 4 distinct indices, maximize (a * b) - (c * d).
# Key idea: biggest product minus smallest product -> nums.sort(), two largest at the end
# (nums[-1], nums[-2]), two smallest at the start (nums[0], nums[1]). Same trick as #1464.
# Gotchas hit: nums[-1] * nums[-1] (same number twice) and a missing `*` between nums[0] nums[1].

from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return ((nums[-1]) * nums[-2] - (nums[0] * nums[1]))


if __name__ == "__main__":
    print(Solution().maxProductDifference([5, 6, 2, 7, 4]))  # 34
    print(Solution().maxProductDifference([4, 2, 5, 9, 7, 4, 8]))  # 64
