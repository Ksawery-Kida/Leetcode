# 1672. Richest Customer Wealth — Easy
# https://leetcode.com/problems/richest-customer-wealth/
# Pattern: array (running max)
# Time: O(m * n) | Space: O(1)
# Key idea: accounts is a list of lists — each inner list = one customer.
# wealth = sum(x) per customer, keep the max in income (overwrite, return AFTER the loop).

class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        income = 0
        for x in accounts:
            wealth = sum(x)
            if wealth > income:
                income = wealth
        return income


if __name__ == "__main__":
    print(Solution().maximumWealth([[1, 2, 3], [3, 2, 1]]))  # 6
    print(Solution().maximumWealth([[1, 5], [7, 3], [3, 5]]))  # 10
    print(Solution().maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]))  # 17
