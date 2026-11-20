# 238. Product of Array Except Self — Medium
# https://leetcode.com/problems/product-of-array-except-self/
# Pattern: prefix / suffix products (two passes, no division)
# Time: O(n) | Space: O(1) extra (besides the answer)
# Problem (summary): answer[i] = product of all numbers except nums[i].
# Key idea: answer[i] = (everything left of i) * (everything right of i).
# Pass 1 (left->right): answer[i] = prefix, THEN prefix *= nums[i].
# Pass 2 (right->left, range(n-1, -1, -1)): answer[x] *= suffix, THEN suffix *= nums[x].
# answer starts as [1] * n so answer[i] exists; 1 is neutral for *.

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = 1
        answer = [1] * len(nums)
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for x in range(len(nums) - 1, -1, -1):
            answer[x] *= suffix
            suffix *= nums[x]
        return answer


if __name__ == "__main__":
    print(Solution().productExceptSelf([1, 2, 3, 4]))  # [24, 12, 8, 6]
    print(Solution().productExceptSelf([-1, 1, 0, -3, 3]))  # [0, 0, 9, 0, 0]

# Redo 2026-11-20: rebuilt step by step. Pass 1 (left -> right): append the running `left`
# product, then left = left * x. Pass 2 (right -> left, range(len(nums) - 1, -1, -1)):
# result[i] = result[i] * right, then right = right * nums[i].
# Mistakes hit: tried `total` (that would need division, which is forbidden); left = nums[i] -
# nums[i-1] (neighbours instead of a running product); `left = left *= nums[x]` (chained = and
# *=, x is a value not an index); second pass appended instead of multiplying result[i];
# range(nums, -1, -1, -1) (needs len(nums) - 1 and three arguments); right * i (index, not value).
#
# class Solution:
#     def productExceptSelf(self, nums: list[int]) -> list[int]:
#         left = 1
#         result = []
#         for x in nums:
#             result.append(left)
#             left = left * x
#         right = 1
#         for i in range(len(nums) - 1, -1, -1):
#             result[i] = result[i] * right
#             right = right * nums[i]
#         return result
