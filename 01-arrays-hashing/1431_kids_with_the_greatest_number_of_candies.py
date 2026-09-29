# 1431. Kids With the Greatest Number of Candies — Easy
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
# Pattern: array (max + compare)
# Time: O(n) | Space: O(n)
# Key idea: biggest = max(candies) once. For each kid append True/False
# (n + extraCandies >= biggest). Append in the loop, return AFTER the loop.

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result = []
        biggest = max(candies)
        for n in candies:
            if (n + extraCandies) >= biggest:
                result.append(True)
            else:
                result.append(False)
        return result


if __name__ == "__main__":
    print(Solution().kidsWithCandies([2, 3, 5, 1, 3], 3))  # [True, True, True, False, True]
    print(Solution().kidsWithCandies([4, 2, 1, 1, 2], 1))  # [True, False, False, False, False]
