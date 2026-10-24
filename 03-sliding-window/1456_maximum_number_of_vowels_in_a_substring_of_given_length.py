# 1456. Maximum Number of Vowels in a Substring of Given Length — Medium
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
# Pattern: sliding window (fixed size k)
# Time: O(n) | Space: O(1)
# Problem (summary): max number of vowels in any substring of length k.
# Key idea: one index c = right end of window. s[c] enters (+1 if vowel),
# s[c - k] leaves (-1 if vowel, only when c >= k). Keep max count.

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        result = 0
        best = 0
        for c in range(len(s)):
            if s[c] in "aeiou":
                result += 1
            if c >= k and s[c - k] in "aeiou":
                result -= 1
            best = max(result, best)
        return best


if __name__ == "__main__":
    print(Solution().maxVowels("abciiidef", 3))  # 3
    print(Solution().maxVowels("aeiou", 2))  # 2
    print(Solution().maxVowels("leetcode", 3))  # 2

# Redo 2026-10-24 (solo): bugs hit — s[c] == "aeiou" compares one letter to the whole string
# (always False, use `in`), and best = max(result, best) was outside the loop (only the last
# window counted) — it must update after every step.
