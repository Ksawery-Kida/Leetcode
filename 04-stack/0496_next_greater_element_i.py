# 496. Next Greater Element I — Easy
# https://leetcode.com/problems/next-greater-element-i/
# Pattern: brute force (nested loops); optimal version uses a monotonic stack
# Time: O(n·m) | Space: O(1) extra (besides the result)
# Problem (summary): for each number in nums1, find the first bigger number to its right in nums2; else -1.
# Key idea: start the inner loop at nums2.index(c) + 1. found = -1 before the inner loop;
# on the first bigger number: found = nums2[j], break. append(found) AFTER the inner loop.

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        for c in nums1:
            found = -1
            for j in range(nums2.index(c) + 1, len(nums2)):
                if nums2[j] > c:
                    found = nums2[j]
                    break
            result.append(found)
        return result


if __name__ == "__main__":
    print(Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))  # [-1, 3, -1]
    print(Solution().nextGreaterElement([2, 4], [1, 2, 3, 4]))  # [3, -1]
