# 387. First Unique Character in a String — Easy
# https://leetcode.com/problems/first-unique-character-in-a-string/
# Pattern: hashing (frequency counter, dict)
# Time: O(n) | Space: O(1) (max 26 letters)
# Key idea: count chars first, then walk the indexes and return the first with count 1.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        for c in s:
            if c in seen:
                seen[c] += 1
            else:
                seen[c] = 1
        for i in range(len(s)):
            c = s[i]
            if seen[c] == 1:
                return i
        return -1


if __name__ == "__main__":
    print(Solution().firstUniqChar("leetcode"))  # 0
    print(Solution().firstUniqChar("loveleetcode"))  # 2
    print(Solution().firstUniqChar("aabb"))  # -1

# Redo 2026-11-15: re-solved from scratch (two passes: count with a dict, then find the first
# index whose letter has count 1). Earlier attempt (2026-11-14) mistakes: used the index as the
# dict key instead of the letter s[x]; checked the count inside the counting loop (a letter
# that repeats later still had count 1); `return -1` in an else ended the loop after one step.
