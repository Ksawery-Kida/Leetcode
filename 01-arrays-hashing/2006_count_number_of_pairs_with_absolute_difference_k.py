# 2006. Count Number of Pairs With Absolute Difference K — Easy
# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/
# Pattern: brute force, nested loops over index pairs
# Time: O(n^2) | Space: O(1)
# Problem (summary): count pairs i < j with |nums[i] - nums[j]| == k.
# Key idea: outer loop over i, inner loop j in range(i + 1, len(nums)) — every pair exactly once,
# never i == j, so no i < j check is needed in the if. abs() is a built-in FUNCTION: abs(a - b).
# (O(n) version later: hashmap counting x - k and x + k.)
# Mistakes hit: `for i and j in nums` (one loop can't give two vars); range(nums) (needs len);
# missing `in`; inner loop from 0 (pairs counted twice / with itself); j = i + 1 inside the loop
# (overwrites j each turn); value comparison nums[i] < nums[j] instead of abs; abs.nums[i],
# abs[...] (abs is a function -> abs(...)) with == k inside the brackets; missing colon.

from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        result = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):

                if abs(nums[i] - nums[j]) == k:
                    result += 1

        return result


if __name__ == "__main__":
    print(Solution().countKDifference([1, 2, 2, 1], 1))  # 4
    print(Solution().countKDifference([1, 3], 3))  # 0
    print(Solution().countKDifference([3, 2, 1, 5, 4], 2))  # 3
