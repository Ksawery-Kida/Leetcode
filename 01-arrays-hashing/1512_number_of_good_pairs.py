# 1512. Number of Good Pairs — Easy
# https://leetcode.com/problems/number-of-good-pairs/
# Pattern: hashing (frequency dict)
# Time: O(n) | Space: O(n)
# Key idea: seen[x] = how many times x appeared so far. A new x forms a pair with each
# earlier x -> pairs += seen[x] BEFORE incrementing seen[x].

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        seen = {}
        pairs = 0
        for x in nums:
            if x in seen:
                pairs += seen[x]
                seen[x] += 1
            else:
                seen[x] = 1
        return pairs


if __name__ == "__main__":
    print(Solution().numIdenticalPairs([1, 2, 3, 1, 1, 3]))  # 4
    print(Solution().numIdenticalPairs([1, 1, 1, 1]))  # 6
    print(Solution().numIdenticalPairs([1, 2, 3]))  # 0
