# 1342. Number of Steps to Reduce a Number to Zero — Easy
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
# Pattern: simulation, while loop + parity check
# Time: O(log n) | Space: O(1)
# Problem (summary): even -> divide by 2, odd -> subtract 1; count steps until 0.
# Key idea: while num != 0: update num ITSELF (num = num // 2 or num = num - 1), count += 1
# once per step (outside the if/else).
# Mistakes hit: `num / 2` without assignment (result lost -> infinite loop); `/` gives a float
# (use //); undefined `x` for the odd case (just else); divided AND subtracted on odd
# (num // 2 - 1) — odd only subtracts 1; stored the result in a new var `calc` instead of num.

class Solution:
    def numberOfSteps(self, num: int) -> int:

        result = 0

        while num != 0:

            if num % 2 == 0:
                num = num // 2

            elif num % 2 != 0:
                num = num - 1

            result += 1

        return result


if __name__ == "__main__":
    print(Solution().numberOfSteps(14))  # 6
    print(Solution().numberOfSteps(8))  # 4
    print(Solution().numberOfSteps(123))  # 12
    print(Solution().numberOfSteps(0))  # 0
