#   Brute Force

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j] 


#   Hash Map
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i in range(len(nums)):
                x = nums[i] 
                need = target - x 
                if need in seen: 
                    return[seen[need], i]
                else:   
                    seen[x] = i


        