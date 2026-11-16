# 347. Top K Frequent Elements — Medium
# https://leetcode.com/problems/top-k-frequent-elements/
# Pattern: hashing (count with a dict) + sort keys by their count
# Time: O(n log n) | Space: O(n)
# Problem (summary): return the k most frequent elements of nums (any order).
# Key idea: count occurrences in a dict, then sort the KEYS by their counts
# (key=dc.get, reverse=True) and take the first k.
# Mistakes hit: sorted(dc) sorts the keys by their own value, not by frequency; key=x passed
# a number instead of a function; sorted inside the counting loop (only needed once, after it).
# Follow-up (O(n)): bucket sort — list of buckets indexed by count.


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dc = {}

        for x in nums:
            if x in dc:
                dc[x] += 1
            else:
                dc[x] = 1

        result = sorted(dc, key=dc.get, reverse=True)
        return result[:k]


if __name__ == "__main__":
    print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
    print(Solution().topKFrequent([1], 1))  # [1]
