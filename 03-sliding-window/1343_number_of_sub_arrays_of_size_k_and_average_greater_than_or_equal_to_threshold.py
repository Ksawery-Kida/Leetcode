# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold — Medium
# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
# Pattern: sliding window (fixed size k)
# Time: O(n) | Space: O(1)
# Problem (summary): count windows of length k whose average >= threshold.
# Key idea: window += arr[i] (enters); if i >= k: window -= arr[i - k] (leaves) BEFORE the check;
# check only when the window is full (i >= k - 1). No else needed.

class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        count = 0
        window = 0
        for i in range(len(arr)):
            window += arr[i]
            if i >= k:
                window -= arr[i - k]
            if i >= k - 1 and window / k >= threshold:
                count += 1
        return count


if __name__ == "__main__":
    print(Solution().numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4))  # 3
    print(Solution().numOfSubarrays([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5))  # 6
