# 1528. Shuffle String — Easy
# https://leetcode.com/problems/shuffle-string/
# Pattern: array, placing values at given positions
# Time: O(n) | Space: O(n)
# Problem (summary): the letter at position i of s goes to position indices[i]; return the string.
# Key idea: pre-size the result with len(s) empty slots ([""] * len(s)) so you can write to any
# position, loop over INDICES (range(len(s))), result[indices[i]] = s[i], then "".join(result).
# Mistakes hit: `for c in s` gives letters, not positions; tried s[c] = ... (strings are immutable);
# typo indicies; loop var c but used i; sides swapped (indices[s]); result = [] empty (IndexError)
# -> [len(s)] (one number) -> [[""] * len(s)] (list inside a list) -> [""] * len(s);
# wrote into indices instead of result; ""join.result() instead of "".join(result);
# append[...] (methods use ()) and append adds at the END, not at a position.

from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

        result = [""] * len(s)

        for c in range(len(s)):
            result[indices[c]] = s[c]

        return "".join(result)


if __name__ == "__main__":
    print(Solution().restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))  # leetcode
    print(Solution().restoreString("abc", [0, 1, 2]))  # abc
