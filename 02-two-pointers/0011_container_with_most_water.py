# 11. Container With Most Water — Medium
# https://leetcode.com/problems/container-with-most-water/
# Pattern: two pointers (opposite ends, move ONE per step)
# Time: O(n) | Space: O(1)
# Key idea: water = (right - left) * min(height[left], height[right]); keep the max.
# Move the LOWER wall: it limits the water, moving the higher one can only make it worse.
# Compare HEIGHTS (height[left] < height[right]), right moves with -= 1.

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        maksimum = 0
        while left < right:
            width = right - left
            h = min(height[left], height[right])
            water = width * h
            if water > maksimum:
                maksimum = water
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maksimum


if __name__ == "__main__":
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
    print(Solution().maxArea([1, 1]))  # 1
