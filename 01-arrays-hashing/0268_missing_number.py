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