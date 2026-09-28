# 739. Daily Temperatures — Medium
# https://leetcode.com/problems/daily-temperatures/
# Pattern: monotonic stack
# Time: O(n) | Space: O(n)
# Key idea: stack holds INDEXES of days still waiting for a warmer day.
# Today warmer than day at stack[-1] -> j = pop, answer[j] = c - j (today's index - waiting index).
# After while -> append today's index. answer starts as zeros = default for days that never get warmer.

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        anwser = [0] * len(temperatures)
        for c, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                j = stack.pop()
                i = c - j
                anwser[j] = i
            stack.append(c)
        return anwser


if __name__ == "__main__":
    print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # [1, 1, 4, 2, 1, 1, 0, 0]
    print(Solution().dailyTemperatures([20, 30, 10, 10, 10, 40]))  # [1, 4, 3, 2, 1, 0]
    print(Solution().dailyTemperatures([30, 60, 90]))  # [1, 1, 0]
