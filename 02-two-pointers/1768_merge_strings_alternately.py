# 1768. Merge Strings Alternately — Easy
# https://leetcode.com/problems/merge-strings-alternately/
# Pattern: index loop (like #1470)
# Time: O(n + m) | Space: O(n + m)
# Problem (summary): merge two strings by taking letters alternately, starting with word1;
# leftover letters of the longer word go at the end.
# Key idea: one loop over indexes up to the LONGER length; append word1[i] then word2[i],
# each only if i < len(that word). Return "".join(merged).

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                merged.append(word1[i])
            if i < len(word2):
                merged.append(word2[i])
        return "".join(merged)


if __name__ == "__main__":
    print(Solution().mergeAlternately("abc", "pqr"))  # "apbqcr"
    print(Solution().mergeAlternately("ab", "pqrs"))  # "apbqrs"
    print(Solution().mergeAlternately("abcd", "pq"))  # "apbqcd"
