# 169. Majority Element — Easy
# https://leetcode.com/problems/majority-element/
# Pattern: hashing (frequency counter, dict)
# Time: O(n) | Space: O(n)
# Key idea: count every number, return the one with count > n // 2.
# return exits the function immediately -> "not found" goes AFTER the loop.
# Bonus (O(1) space): Boyer-Moore voting.

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        seen = {}
        for c in nums:
            if c in seen:
                seen[c] += 1
            else:
                seen[c] = 1
        for c in seen:
            if seen[c] > len(nums) // 2:
                return c
        return -1


if __name__ == "__main__":
    print(Solution().majorityElement([3, 2, 3]))  # 3
    print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))  # 2
    print(Solution().majorityElement([1, 2, 2]))  # 2
