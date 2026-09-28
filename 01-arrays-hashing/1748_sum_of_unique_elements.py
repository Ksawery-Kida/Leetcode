# 1748. Sum of Unique Elements — Easy
# https://leetcode.com/problems/sum-of-unique-elements/
# Pattern: hashing (frequency dict)
# Time: O(n) | Space: O(n)
# Key idea: first loop counts occurrences in the dict. Second loop over the keys:
# add x to result only if elements[x] == 1. Return AFTER the loop, not inside.

class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        elements = {}
        result = 0
        for x in nums:
            if x in elements:
                elements[x] += 1
            else:
                elements[x] = 1
        for x in elements:
            if elements[x] == 1:
                result += x
        return result


if __name__ == "__main__":
    print(Solution().sumOfUnique([1, 2, 3, 2]))  # 4
    print(Solution().sumOfUnique([1, 1, 1, 1, 1]))  # 0
    print(Solution().sumOfUnique([1, 2, 3, 4, 5]))  # 15
