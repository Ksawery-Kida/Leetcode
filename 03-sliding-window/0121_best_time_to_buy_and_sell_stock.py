# 121. Best Time to Buy and Sell Stock — Easy
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Pattern: sliding window / running min
# Time: O(n) | Space: O(1)
# Problem (summary): prices[i] = stock price on day i. Buy one day, sell on a LATER day;
# return the max profit (0 if no profit is possible).
# Key idea: remember the lowest price so far (min_price = prices[0], not 0).
# Each day: profit candidate = today - min_price; keep the best; then update min_price.
# max(prices) - min(prices) is WRONG: the max can come before the min.

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        min_price = prices[0]
        for i in prices:
            x = i - min_price
            if x > profit:
                profit = x
            if i < min_price:
                min_price = i
        return profit


if __name__ == "__main__":
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))  # 5
    print(Solution().maxProfit([7, 6, 4, 3, 1]))  # 0
