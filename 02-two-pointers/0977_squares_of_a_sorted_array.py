# 977. Squares of a Sorted Array — Easy
# https://leetcode.com/problems/squares-of-a-sorted-array/
# Pattern: square + sort (two pointers O(n) version is the follow-up)
# Time: O(n log n) | Space: O(n)
# Key idea: square every number, then sort ONCE (no loop around .sort()).

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        squares = []
        for x in nums:
            squares.append(x ** 2)
        squares.sort()
        return squares


if __name__ == "__main__":
    print(Solution().sortedSquares([-4, -1, 0, 3, 10]))  # [0, 1, 9, 16, 100]
    print(Solution().sortedSquares([-7, -3, 2, 3, 11]))  # [4, 9, 9, 49, 121]
