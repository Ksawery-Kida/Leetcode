# 485. Max Consecutive Ones — Easy
# https://leetcode.com/problems/max-consecutive-ones/
# Pattern: counter (first solved with a stack, then simplified)
# Time: O(n) | Space: O(1)
# Problem (summary): length of the longest run of 1s in a binary array.
# Key idea: count += 1 on a 1, count = 0 on a 0; result = max(result, count).
# Stack version: append on 1, clear() on 0, len(stack) = current run — same thing.

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count = 0
        result = 0
        for x in nums:
            if x == 1:
                count += 1
                result = max(result, count)
            else:
                count = 0
        return result


if __name__ == "__main__":
    print(Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))  # 3
    print(Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))  # 2
