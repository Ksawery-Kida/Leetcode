# 283. Move Zeroes — Easy
# https://leetcode.com/problems/move-zeroes/
# Pattern: two pointers (same direction)
# Time: O(n) | Space: O(1)
# Key idea: insert = where the next non-zero goes. i walks every index; when nums[i] != 0
# (VALUE, not index) swap nums[insert] <-> nums[i] and insert += 1. Zeros drift to the end.

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        insert = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert], nums[i] = nums[i], nums[insert]
                insert += 1


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums)
    print(nums)  # [1, 3, 12, 0, 0]
    nums = [0]
    Solution().moveZeroes(nums)
    print(nums)  # [0]
