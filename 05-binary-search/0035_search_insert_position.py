# 35. Search Insert Position — Easy
# https://leetcode.com/problems/search-insert-position/
# Pattern: binary search
# Time: O(log n) | Space: O(1)
# Key idea: classic binary search (while left <= right, mid = (left + right) // 2 — // not /, index must be int).
# Found -> return mid (the INDEX, not the value). target bigger -> left = mid + 1, smaller -> right = mid - 1.
# Not found -> after the loop return left: everything left of `left` is < target, so when the pointers
# cross, left sits on the first number bigger than target = the insert position.

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


if __name__ == "__main__":
    print(Solution().searchInsert([1, 3, 5, 6], 5))  # 2
    print(Solution().searchInsert([1, 3, 5, 6], 2))  # 1
    print(Solution().searchInsert([1, 3, 5, 6], 7))  # 4
