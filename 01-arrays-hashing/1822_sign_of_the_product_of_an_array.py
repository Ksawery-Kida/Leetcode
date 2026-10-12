# 1822. Sign of the Product of an Array — Easy
# https://leetcode.com/problems/sign-of-the-product-of-an-array/
# Pattern: running product (Python ints never overflow)
# Time: O(n) | Space: O(1)
# Problem (summary): product = all numbers multiplied; return 1 / -1 / 0 for its sign.
# Key idea: count = 1 (neutral for *), count *= x in the loop, sign check AFTER the loop.
# Alternative: count negatives (odd -> -1), any 0 -> 0.

class Solution:
    def arraySign(self, nums: list[int]) -> int:
        count = 1
        for x in nums:
            count *= x
        if count > 0:
            return 1
        elif count < 0:
            return -1
        else:
            return 0


if __name__ == "__main__":
    print(Solution().arraySign([-1, -2, -3, -4, 3, 2, 1]))  # 1
    print(Solution().arraySign([1, 5, 0, 2, -3]))  # 0
    print(Solution().arraySign([-1, 1, -1, 1, -1]))  # -1
