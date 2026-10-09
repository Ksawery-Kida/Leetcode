# 1137. N-th Tribonacci Number — Easy
# https://leetcode.com/problems/n-th-tribonacci-number/
# Pattern: dynamic programming (bottom-up, same as #509 but 3 previous values)
# Time: O(n) | Space: O(n)
# Key idea: start with [0, 1, 1] (need THREE previous), append numbers[-1] + numbers[-2] + numbers[-3].
# Loop could start at 3 (range(3, n + 1)); starting at 2 still works, it just builds one extra element.

class Solution:
    def tribonacci(self, n: int) -> int:
        numbers = [0, 1, 1]
        for x in range(2, n + 1):
            numbers.append(numbers[-1] + numbers[-2] + numbers[-3])
        return numbers[n]


if __name__ == "__main__":
    print(Solution().tribonacci(4))   # 4
    print(Solution().tribonacci(25))  # 1389537
    print(Solution().tribonacci(0))   # 0
