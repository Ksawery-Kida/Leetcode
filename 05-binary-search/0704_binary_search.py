# 704. Binary Search — Easy
# https://leetcode.com/problems/binary-search/
# Pattern: binary search
# Time: O(log n) | Space: O(1)
# Key idea: sorted input -> check the middle, throw away the half that can't contain target.
# left/right are INDEXES. +1/-1 because mid was already checked.

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


if __name__ == "__main__":
    print(Solution().search([-1, 0, 3, 5, 9, 12], 9))  # 4
    print(Solution().search([-1, 0, 3, 5, 9, 12], 2))  # -1
    print(Solution().search([5], 5))  # 0
