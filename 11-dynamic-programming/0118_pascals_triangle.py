# 118. Pascal's Triangle — Easy
# https://leetcode.com/problems/pascals-triangle/
# Pattern: dynamic programming (each row built from the previous row)
# Time: O(n^2) | Space: O(n^2)
# Key idea: list of lists. Every row starts with [1]; from the 2nd row on (x > 0), each middle number
# = Triangle[-1][j - 1] + Triangle[-1][j] (two neighbours from the previous row), then append(1) at the end.
# Big jump vs #509/#1137: nested loop + list of lists + double index [-1][j]. Needs a re-walkthrough.

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        Triangle = []
        for x in range(numRows):
            row = [1]
            if x > 0:
                for j in range(1, len(Triangle[-1])):
                    row.append(Triangle[-1][j - 1] + Triangle[-1][j])
                row.append(1)
            Triangle.append(row)
        return Triangle


if __name__ == "__main__":
    print(Solution().generate(5))  # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    print(Solution().generate(1))  # [[1]]
