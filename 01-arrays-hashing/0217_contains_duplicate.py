# 217. Contains Duplicate — Easy
# https://leetcode.com/problems/contains-duplicate/
# Pattern: hashing (set)
# Time: O(n) | Space: O(n)
# Key idea: remember seen numbers; check before adding.
# Brute force (nested loops over all pairs) is O(n^2) -> TLE for n = 10^5.

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


if __name__ == "__main__":
    print(Solution().containsDuplicate([1, 2, 3, 1]))  # True
    print(Solution().containsDuplicate([1, 2, 3, 4]))  # False
    print(Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True
# Redo 2026-11-09: re-solved from scratch, first try.
# Redo 2026-11-24: re-solved from scratch (renamed loop variable to num).
