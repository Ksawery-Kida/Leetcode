# 1470. Shuffle the Array — Easy
# https://leetcode.com/problems/shuffle-the-array/
# Pattern: array (index math)
# Time: O(n) | Space: O(n)
# Key idea: the pair of nums[i] is always n indexes later -> nums[i + n].
# Loop over INDEXES with range(n), two appends per step. "+ n" goes INSIDE the brackets.

class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i + n])
        return result


if __name__ == "__main__":
    print(Solution().shuffle([2, 5, 1, 3, 4, 7], 3))  # [2, 3, 5, 4, 1, 7]
    print(Solution().shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4))  # [1, 4, 2, 3, 3, 2, 4, 1]
