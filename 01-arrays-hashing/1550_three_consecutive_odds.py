# 1550. Three Consecutive Odds — Easy
# https://leetcode.com/problems/three-consecutive-odds/
# Pattern: counter of a run (same as #485)
# Time: O(n) | Space: O(1)
# Problem (summary): are there three odd numbers in a row?
# Key idea: odd -> count += 1 (return True at 3), even -> count = 0. return False AFTER the loop.

class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        count = 0
        for x in arr:
            if x % 2:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0
        return False


if __name__ == "__main__":
    print(Solution().threeConsecutiveOdds([2, 6, 4, 1]))  # False
    print(Solution().threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 23, 12]))  # True
    print(Solution().threeConsecutiveOdds([1, 2, 1, 2, 1]))  # False
