# 242. Valid Anagram — Easy
# https://leetcode.com/problems/valid-anagram/
# Pattern: hashing (frequency counter, dict)
# Time: O(n) | Space: O(n)
# Key idea: count every char in s and in t, then compare the two dicts.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        licznik_s = {}
        licznik_t = {}
        for c in s:
            if c in licznik_s:
                licznik_s[c] += 1
            else:
                licznik_s[c] = 1
        for c in t:
            if c in licznik_t:
                licznik_t[c] += 1
            else:
                licznik_t[c] = 1
        return licznik_s == licznik_t


if __name__ == "__main__":
    print(Solution().isAnagram("anagram", "nagaram"))  # True
    print(Solution().isAnagram("rat", "car"))  # False
