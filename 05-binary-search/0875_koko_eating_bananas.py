# 875. Koko Eating Bananas — Medium
# https://leetcode.com/problems/koko-eating-bananas/
# Pattern: binary search on the answer (search over possible k, not over a list)
# Time: O(n * log(max(piles))) | Space: O(1)
# Pure numbers: find the smallest k in [1, max(piles)] such that sum(ceil(p / k)) <= h.
# Bigger k -> fewer hours (monotonic) -> binary search. k > max(piles) never helps (1 hour per pile minimum).
# hours = 0 must be reset INSIDE the while (new count for every mid). ceil(x / mid), with / not //.
# Fits -> right = mid - 1 (try smaller), too slow -> left = mid + 1. Return left (like #35).

import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for x in piles:
                hours += math.ceil(x / mid)
            if hours <= h:
                right = mid - 1
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    print(Solution().minEatingSpeed([3, 6, 7, 11], 8))  # 4
    print(Solution().minEatingSpeed([30, 11, 23, 4, 20], 5))  # 30
