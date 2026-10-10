# 1365. How Many Numbers Are Smaller Than the Current Number — Easy
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
# Pattern: brute force (nested loops)
# Time: O(n^2) | Space: O(n)
# Problem (summary): for each number, how many numbers in the array are smaller.
# Key idea: outer loop picks i, inner loop counts j < i; reset count per i, append after inner loop.

class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        result = []
        for i in nums:
            count = 0
            for j in nums:
                if j < i:
                    count += 1
            result.append(count)
        return result


if __name__ == "__main__":
    print(Solution().smallerNumbersThanCurrent([8, 1, 2, 2, 3]))  # [4, 0, 1, 1, 3]
    print(Solution().smallerNumbersThanCurrent([7, 7, 7, 7]))  # [0, 0, 0, 0]
