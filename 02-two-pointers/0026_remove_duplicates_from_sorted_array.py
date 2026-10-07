# 26. Remove Duplicates from Sorted Array — Easy
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Pattern: two pointers, same direction (insert index, like #283)
# Time: O(n) | Space: O(1)
# Key idea: modify nums IN PLACE — a set/new list gives the count but leaves nums unchanged (judge checks first k slots).
# Sorted -> duplicates sit next to each other: new number <=> nums[i] != nums[i - 1].
# result = how many uniques so far = next free slot. Write nums[result] = nums[i] (left side = where you write).
# Loop starts at 1 (range(1, len(nums))): at i = 0, nums[i - 1] is nums[-1] = LAST element -> false "new".
# TODO: study again later ("mega dziwne") — why overwriting the front never loses data (result <= i always).

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        result = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[result] = nums[i]
                result += 1
        return result


if __name__ == "__main__":
    a = [1, 1, 2]
    print(Solution().removeDuplicates(a), a[:2])  # 2 [1, 2]
    b = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(Solution().removeDuplicates(b), b[:5])  # 5 [0, 1, 2, 3, 4]
