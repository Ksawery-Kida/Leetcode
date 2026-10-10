# 1351. Count Negative Numbers in a Sorted Matrix — Easy
# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
# Pattern: brute force (nested loops over a matrix)
# Time: O(m·n) | Space: O(1)
# Problem (summary): count numbers < 0 in a 2D grid.
# Key idea: outer loop = rows (each row is a list), inner loop = numbers in the row; no reset.

class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        count = 0
        for x in grid:
            for c in x:
                if c < 0:
                    count += 1
        return count


if __name__ == "__main__":
    print(Solution().countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))  # 8
    print(Solution().countNegatives([[3, 2], [1, 0]]))  # 0
