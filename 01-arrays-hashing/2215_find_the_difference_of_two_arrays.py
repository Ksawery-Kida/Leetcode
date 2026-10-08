# 2215. Find the Difference of Two Arrays — Easy
# https://leetcode.com/problems/find-the-difference-of-two-arrays/
# Pattern: hashing (set for distinct results)
# Time: O(n * m) with list lookups (O(n + m) if nums1/nums2 were turned into sets) | Space: O(n + m)
# Key idea: two separate loops (a for goes over ONE list), each fills its OWN set (no duplicates, add not append).
# Return a list of two lists: [list(missing1), list(missing2)].

class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        missing1 = set()
        missing2 = set()
        for c in nums1:
            if c not in nums2:
                missing1.add(c)
        for c in nums2:
            if c not in nums1:
                missing2.add(c)
        return [list(missing1), list(missing2)]


if __name__ == "__main__":
    print(Solution().findDifference([1, 2, 3], [2, 4, 6]))  # [[1, 3], [4, 6]]
    print(Solution().findDifference([1, 2, 3, 3], [1, 1, 2, 2]))  # [[3], []]
