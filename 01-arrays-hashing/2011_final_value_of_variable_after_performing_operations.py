# 2011. Final Value of Variable After Performing Operations — Easy
# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
# Pattern: array (simulation)
# Time: O(n) | Space: O(1)
# Key idea: one counter, +1 for "++X"/"X++", -1 for "--X"/"X--".
# GOTCHA: `op == "++X" or "X++"` is ALWAYS True (non-empty string is truthy).
# Write `op == "++X" or op == "X++"`.

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
