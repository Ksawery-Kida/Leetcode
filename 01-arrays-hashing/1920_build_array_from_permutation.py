# 1920. Build Array from Permutation — Easy
# https://leetcode.com/problems/build-array-from-permutation/
# Pattern: array (index math)
# Time: O(n) | Space: O(n)
# Key idea: ans[i] = nums[nums[i]]. Looping over values, x is already nums[i] -> append nums[x].

class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans = []
        for x in nums:
            ans.append(nums[x])
        return ans


if __name__ == "__main__":
    print(Solution().buildArray([0, 2, 1, 5, 3, 4]))  # [0, 1, 2, 4, 5, 3]
    print(Solution().buildArray([5, 0, 1, 2, 3, 4]))  # [4, 5, 0, 1, 2, 3]
