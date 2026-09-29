# 167. Two Sum II - Input Array Is Sorted — Medium
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Pattern: two pointers (opposite ends, move ONE per step)
# Time: O(n) | Space: O(1)
# Key idea: sorted input. total = numbers[left] + numbers[right].
# Too big -> right -= 1 (smaller numbers are left of right). Too small -> left += 1.
# Equal -> return [left + 1, right + 1] (1-indexed). vs #1: dict O(n) space, here O(1).

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total > target:
                right -= 1
            elif total < target:
                left += 1
            else:
                return [left + 1, right + 1]
        return []


if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15], 9))  # [1, 2]
    print(Solution().twoSum([2, 3, 4], 6))  # [1, 3]
    print(Solution().twoSum([-1, 0], -1))  # [1, 2]
