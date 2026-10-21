#   Brute Force

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j] 


#   Hash Map — O(n): seen = {value: index} of numbers already passed; for each x ask "was
#   target - x already seen?" -> yes = [seen[need], i]. Dict `in` is O(1), so no second loop.
#   Redo 2026-10-21: re-solved it alone after first being scared by this code.
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


        