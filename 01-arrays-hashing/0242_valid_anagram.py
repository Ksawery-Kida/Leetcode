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

# Redo 2026-11-12: re-solved with a different approach — sort both strings and compare.
# Time: O(n log n) | Space: O(n). Simpler to write, slower than the dict counter.
# Mistakes hit: NameError (used an undefined variable inside sorted()).
# (the while loop is not needed — the body returns on the first pass)
#
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         while s and t:
#             if sorted(s) != sorted(t):
#                 return False
#             else:
#                 return True
