# 1480. Running Sum of 1d Array — Easy
# https://leetcode.com/problems/running-sum-of-1d-array/
# Pattern: prefix sum
# Time: O(n) | Space: O(n)
# Key idea: keep a running total (a number, not a set/list), add each x, append the total.

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result = []
        total = 0
        for x in nums:
            total += x
            result.append(total)
        return result


if __name__ == "__main__":
    print(Solution().runningSum([1, 2, 3, 4]))  # [1, 3, 6, 10]
    print(Solution().runningSum([1, 1, 1, 1, 1]))  # [1, 2, 3, 4, 5]
    print(Solution().runningSum([3, 1, 2, 10, 1]))  # [3, 4, 6, 16, 17]
