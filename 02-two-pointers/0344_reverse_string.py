# 344. Reverse String — Easy
# https://leetcode.com/problems/reverse-string/
# Pattern: two pointers (opposite ends)
# Time: O(n) | Space: O(1)
# Key idea: left = 0, right = len(s) - 1 (INDEXES). While left < right: swap, move both inward.
# Swap in one line: s[left], s[right] = s[right], s[left]

class Solution:
    def reverseString(self, s: list[str]) -> None:
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    Solution().reverseString(s)
    print(s)  # ['o', 'l', 'l', 'e', 'h']
    s = ["H", "a", "n", "n", "a", "h"]
    Solution().reverseString(s)
    print(s)  # ['h', 'a', 'n', 'n', 'a', 'H']
