# 2011. Final Value of Variable After Performing Operations — Easy
# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
# Pattern: array (simulation)
# Time: O(n) | Space: O(1)
# Key idea: one counter, +1 for "++X"/"X++", -1 for "--X"/"X--".
# GOTCHA: `op == "++X" or "X++"` is ALWAYS True (non-empty string is truthy).
# Write `op == "++X" or op == "X++"`.
#
# Problem (summary): X starts at 0. operations is a list of "++X", "X++" (X += 1)
# and "--X", "X--" (X -= 1). Return the final value of X.
#
# My first attempt (bug):
#     if op == "++X" or "X++":
# Python reads this as (op == "++X") or ("X++"). A non-empty string is always truthy,
# so the condition is ALWAYS True -> every operation added 1 -> wrong answer.
# Fix: repeat the full comparison after `or`:  op == "++X" or op == "X++"
# (or give each operation its own if/elif, like the accepted version below).

class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        result = 0
        for op in operations:
            if op == "++X":
                result += 1
            elif op == "X++":
                result += 1
            elif op == "--X":
                result -= 1
            elif op == "X--":
                result -= 1
        return result


if __name__ == "__main__":
    print(Solution().finalValueAfterOperations(["--X", "X++", "X++"]))  # 1
    print(Solution().finalValueAfterOperations(["++X", "++X", "X++"]))  # 3
    print(Solution().finalValueAfterOperations(["X++", "++X", "--X", "X--"]))  # 0
