class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        seen = set(nums)
        for x in range(n+1):
            if x not in seen:
                return x 



        