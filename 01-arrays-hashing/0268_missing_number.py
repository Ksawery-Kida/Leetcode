class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        seen = set(nums)
        for x in range(n+1):
            if x not in seen:
                return x 

#   1. n = len(nums) - wyliczamy dlugosc listy nums
#   2. seen = set(nums) - tworzymy zbior z elementow listy nums
#   3. for x in range(n+1): - lecimy kolejno po liczbach 
#   4. If x not in seen: - sprawdzam czy liczba "x" jest w zbiorze seen
#   5. return x - zwracamy liczbe ktora nie jest w zbiorze seen
# Redo 2026-11-13: re-solved from scratch. Mistakes hit: looped over a copy of nums (the missing
# number is never in nums, so it was never found); range(len(nums)) missed n itself ([0,1] -> 2).
# Note: `i not in nums` on a LIST is O(n) per check -> O(n^2) total; the set version above is O(n).
#
# class Solution:
#     def missingNumber(self, nums: list[int]) -> int:
#         seen = []
#         for x in range(len(nums) + 1):
#             seen.append(x)
#         for i in seen:
#             if i not in nums:
#                 return i
