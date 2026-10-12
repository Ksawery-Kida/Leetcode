# 2574. Left and Right Sum Differences — Easy
# https://leetcode.com/problems/left-and-right-sum-differences/
# Pattern: prefix / suffix sums (same idea as #238, with + instead of *)
# Time: O(n) | Space: O(1) extra (besides the answer)
# Problem (summary): for each i, |sum of everything left of i - sum of everything right of i|.
# Key idea: the loop index is the "finger". Pass 1 (left->right): store pref BEFORE adding nums[x].
# Pass 2 (right->left): answer[x] = abs(answer[x] - suff), then add nums[x] to suff. Sums start at 0.

from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        pref = 0
        anwser = [1] * len(nums)
        for x in range(len(nums)):
            anwser[x] = pref
            pref += nums[x]
        suff = 0
        for x in range(len(nums) - 1, -1, -1):
            anwser[x] = abs(anwser[x] - suff)
            suff += nums[x]
        return anwser


if __name__ == "__main__":
    print(Solution().leftRightDifference([10, 4, 8, 3]))  # [15, 1, 11, 22]
    print(Solution().leftRightDifference([1]))  # [0]
