# 1464. Maximum Product of Two Elements in an Array — Easy
# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
# Pattern: array, sorting
# Time: O(n log n) | Space: O(1) (in-place sort)
# Problem (summary): return the max of (nums[i] - 1) * (nums[j] - 1) for i != j.
# Key idea: the answer always uses the two largest numbers -> nums.sort() (ascending, in place),
# they end up at nums[-1] and nums[-2] (same negative indexing as stack[-1]). No loop needed.
# Note: result/outcome variables are redundant — could `return (nums[-1] - 1) * (nums[-2] - 1)`.
# O(n) alternative: one pass tracking the biggest and second biggest.

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        result = 0
        nums.sort()
        outcome = ((nums[-1] - 1) * (nums[-2] - 1))
        result = outcome
        return result


if __name__ == "__main__":
    print(Solution().maxProduct([3, 4, 5, 2]))  # 12
    print(Solution().maxProduct([1, 5, 4, 5]))  # 16
    print(Solution().maxProduct([3, 7]))  # 12
