# 2089. Find Target Indices After Sorting Array — Easy
# https://leetcode.com/problems/find-target-indices-after-sorting-array/
# Pattern: sorting + index loop
# Time: O(n log n) | Space: O(n)
# Problem (summary): sort nums, return all indices where the value equals target (or []).
# Key idea: s = sorted(nums), loop over INDICES (range(len(s))), append i when s[i] == target.
# If target is missing, result just stays [] — no special case needed.
# (O(n) trick: count numbers < target and == target -> indices are range(less, less + equal).)
# Mistakes hit: for x in s (values) then s[x] (value used as index); return inside the loop
# (stops at the first hit); returned the value instead of the index; -1 instead of [];
# append[x] instead of append(x); `if not target` checks target == 0, not "not found".

from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        s = sorted(nums)
        result = []

        for x in range(len(s)):

            if s[x] == target:
                result.append(x)

        return result


if __name__ == "__main__":
    print(Solution().targetIndices([1, 2, 5, 2, 3], 2))  # [1, 2]
    print(Solution().targetIndices([1, 2, 5, 2, 3], 5))  # [4]
    print(Solution().targetIndices([1, 2, 5, 2, 3], 4))  # []
