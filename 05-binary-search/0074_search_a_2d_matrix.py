# 74. Search a 2D Matrix — Medium
# https://leetcode.com/problems/search-a-2d-matrix/
# Pattern: binary search (2D matrix treated as one sorted list)
# Time: O(log(m * n)) | Space: O(1)
# Key idea: rows sorted + each row starts above the previous row's end -> reading rows one after another
# gives ONE sorted list. Don't build it (that's O(m*n)) — binary search over indices 0 .. rows*cols - 1.
# Index -> cell: row = mid // cols (how many full rows come before mid), col = mid % cols (what's left).
# value = matrix[mid // m][mid % m]; compare VALUE (not mid) with target. return False AFTER the loop.
# Note: here n = rows, m = cols (opposite of the problem statement — what matters is what YOU assigned).

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        left = 0
        right = (m * n) - 1
        while left <= right:
            mid = (left + right) // 2
            value = matrix[mid // m][mid % m]
            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


if __name__ == "__main__":
    grid = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    print(Solution().searchMatrix(grid, 3))   # True
    print(Solution().searchMatrix(grid, 13))  # False
