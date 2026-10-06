# 1295. Find Numbers with Even Number of Digits — Easy
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
# Pattern: array (counter)
# Time: O(n * d) | Space: O(d)  (d = digits per number)
# Key idea: digit count = len(str(c)) — len works on strings, not ints.
# Even check = remainder % 2 == 0 (not / , and == not =). Loop var name must match.

class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        result = 0
        for c in nums:
            if len(str(c)) % 2 == 0:
                result += 1
        return result


if __name__ == "__main__":
    print(Solution().findNumbers([12, 345, 2, 6, 7896]))  # 2
    print(Solution().findNumbers([555, 901, 482, 1771]))  # 1
