# 1389. Create Target Array in the Given Order — Easy
# https://leetcode.com/problems/create-target-array-in-the-given-order/
# Pattern: array, list.insert at given positions
# Time: O(n^2) (each insert shifts elements) | Space: O(n)
# Problem (summary): start empty; for each i insert nums[i] at position index[i]; return target.
# Key idea: target = [] and target.insert(index[i], nums[i]) — insert SHIFTS the rest right,
# while target[i] = ... would OVERWRITE. Loop over indices: range(len(nums)).
# Mistakes hit: target = [len(nums)] (one number, not empty); while nums and index (never empties
# -> infinite loop); nums(x) instead of nums[x]; wrote into index instead of target; tried
# target += int; insert[...] instead of insert(...); index[] empty; missing comma / colon.
# Recurring: method calls use () — append(...), insert(...), sort().

from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []

        for x in range(len(nums)):
            target.insert(index[x], nums[x])

        return target


if __name__ == "__main__":
    print(Solution().createTargetArray([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]))  # [0, 4, 1, 3, 2]
    print(Solution().createTargetArray([1, 2, 3, 4, 0], [0, 1, 2, 3, 0]))  # [0, 1, 2, 3, 4]
