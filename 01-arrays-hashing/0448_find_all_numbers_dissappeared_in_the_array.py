class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums) 
        seen = set(nums)
        missing = []
        for x in range(1, n+1):
            if x not in seen: 
                missing.append(x)
        return missing 
                

#  1. n = len(nums) - wyliczamy dlugosc listy nums
#  2. seen = set(nums) - tworzymy zbior z elementow listy nums
#  3. missing = [] - tworzymy pusta liste na brakujacych liczb 
#  4. for x in range(1, n+1): - lecimy kolejno po liczbach od 1 do n
#  5. If x not in seen: - sprawdzam czy liczba "x" jest w zbiorze seen
#  6. missing.append(x) - dodaje brakujaca liczbe do listy missing
#  7. return missing - printuje liste missing liczb
