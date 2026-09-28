# 1394. Find Lucky Integer in an Array — Easy
# https://leetcode.com/problems/find-lucky-integer-in-an-array/
# Pattern: hashing (frequency dict)
# Time: O(n) | Space: O(n)
# Key idea: count occurrences, then over the keys keep the largest x with count[x] == x.
# result starts at -1 = the answer when no lucky number exists (no return inside the loop).

class Solution:
    def findLucky(self, arr: list[int]) -> int:
        count = {}
        result = -1
        for x in arr:
            if x in count:
                count[x] += 1
            else:
                count[x] = 1
        for x in count:
            if x > result and x == count[x]:
                result = x
        return result


if __name__ == "__main__":
    print(Solution().findLucky([2, 2, 3, 4]))  # 2
    print(Solution().findLucky([1, 2, 2, 3, 3, 3]))  # 3
    print(Solution().findLucky([2, 2, 2, 3, 3]))  # -1
