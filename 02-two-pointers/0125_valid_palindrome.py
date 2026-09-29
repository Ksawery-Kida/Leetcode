# 125. Valid Palindrome — Easy
# https://leetcode.com/problems/valid-palindrome/
# Pattern: two pointers (opposite ends)
# Time: O(n) | Space: O(n)
# Key idea: build a cleaned list (c.isalnum() -> letters/digits only, c.lower()).
# right = len(letters) - 1 AFTER building it. Compare first, then move pointers.
# Follow-up: O(1) space by skipping non-alnum chars with the pointers directly on s.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = []
        left = 0
        for c in s:
            if c.isalnum():
                letters.append(c.lower())
        right = len(letters) - 1
        while left < right:
            if letters[left] != letters[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))  # True
    print(Solution().isPalindrome("race a car"))  # False
    print(Solution().isPalindrome(" "))  # True
    print(Solution().isPalindrome("0P"))  # False
