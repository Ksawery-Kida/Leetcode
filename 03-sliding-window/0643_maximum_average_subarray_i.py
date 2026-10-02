# 643. Maximum Average Subarray I — Easy
# https://leetcode.com/problems/maximum-average-subarray-i/
# Pattern: sliding window (fixed size k)
# Time: O(n) | Space: O(1)
# Problem (summary): find k consecutive numbers with the largest average; return that average.
# Key idea: window = sum of the first k. Slide right: add nums[i] (enters), subtract
# nums[i - k] (leaves). Keep the best SUM, return best / k at the end.

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        best = sum(nums[:k])
        window = sum(nums[:k])
        for i in range(k, len(nums)):
            window += nums[i] - nums[i - k]
            if window > best:
                best = window
        return best / k


if __name__ == "__main__":
    print(Solution().findMaxAverage([1, 12, -5, -6, 50, 3], 4))  # 12.75
    print(Solution().findMaxAverage([5], 1))  # 5.0
