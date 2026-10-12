# 724. Find Pivot Index — Easy
# https://leetcode.com/problems/find-pivot-index/
# Pattern: prefix sum (left sum + total)
# Time: O(n) | Space: O(1)
# Problem (summary): leftmost index where sum of numbers to the left == sum to the right; else -1.
# Key idea: total = sum(nums), left starts at 0 (sum of nothing).
# right = total - left - nums[x]. If equal -> return x, else add nums[x] to left.

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        left = 0
        for x in range(len(nums)):
            right = total - left - nums[x]
            if right == left:
                return x
            else:
                left += nums[x]
        return -1


if __name__ == "__main__":
    print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))  # 3
    print(Solution().pivotIndex([1, 2, 3]))  # -1
    print(Solution().pivotIndex([2, 1, -1]))  # 0
