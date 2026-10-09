# 509. Fibonacci Number — Easy
# https://leetcode.com/problems/fibonacci-number/
# Pattern: dynamic programming (bottom-up, store previous results in a list)
# Time: O(n) | Space: O(n)
# Key idea: start with [0, 1], each step append numbers[-1] + numbers[-2], answer = numbers[n].
# list += int -> TypeError (use append). Return numbers[n], not numbers[x] (x doesn't exist for n < 2).

class Solution:
    def fib(self, n: int) -> int:
        numbers = [0, 1]
        for x in range(2, n + 1):
            numbers.append(numbers[-1] + numbers[-2])
        return numbers[n]


if __name__ == "__main__":
    print(Solution().fib(2))  # 1
    print(Solution().fib(4))  # 3
    print(Solution().fib(0))  # 0
