# 3727. Maximum Alternating Sum of Squares — Medium
# https://leetcode.com/problems/maximum-alternating-sum-of-squares/
# Pattern: greedy + sorting
# Time: O(n log n) | Space: O(n)
# Problem (summary): rearrange nums freely; score = a0² - a1² + a2² - ...; return the max score.
# Key idea: order is free, so score = (sum of squares on + slots) - (sum on - slots). Put the
# BIGGEST squares on + and the smallest on -. Squares make negatives positive (-5 -> 25), so square
# first, then sort. Plus slots = even positions = ceil(n/2) = (n + 1) // 2 (+1 before // rounds up).
# Answer: sum(sq[-k:]) - sum(sq[:-k]). n up to 1e5 -> O(n log n) is fine, no nested loops.
# Alternative (shorter): count the MINUS slots instead = n // 2 (no rounding trick):
# return sum(sq[n // 2:]) - sum(sq[:n // 2]).
# Mistakes hit: nums[x] with x already a value; stray colon after an expression; sort(rslt) /
# rslt(sort) instead of rslt.sort(); (x + 1) // 2 with the loop var instead of len(nums);
# len(nums) = length (assignment reversed); undefined `best`; subtracted sum(nums) (originals,
# all of them) instead of the rest of the squares. Final line was given.

from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        rslt = []  # lista z result

        for x in nums:  # petla po liczbach + ich potegowanie
            rslt.append(x ** 2)

        rslt.sort()  # sort
        length = len(nums)  # dlugosc pod equation

        most = (length + 1) // 2  # equation pod most wynik
        outcome = sum(rslt[-most:]) - sum(rslt[:-most])  # outcome

        return outcome


if __name__ == "__main__":
    print(Solution().maxAlternatingSum([1, 2, 3]))  # 9 + 1 - 4 = 12
    print(Solution().maxAlternatingSum([1, -1, 2, -2, 3, -3]))  # (9+9+4) - (4+1+1) = 16
    print(Solution().maxAlternatingSum([5]))  # 25
