# 49. Group Anagrams — Medium (NeetCode 150)
# https://leetcode.com/problems/group-anagrams/
# Pattern: hashing (dict: key -> list of words)
# Time: O(n * k log k), k = max word length | Space: O(n * k)
# Problem (summary): group the words that are anagrams of each other.
# Key idea: all anagrams give the same string after sorting their letters ("eat", "tea", "ate"
# -> "aet"). Use that sorted string as the dict key and keep a LIST of words as the value:
# new key -> start a list [x]; existing key -> append x. The groups are dct.values().
# Mistakes hit: stack idea (anagrams are not adjacent, groups can have > 2 words); counting like
# #169 instead of storing words; .split().sort() (split cuts on spaces, sort() returns None);
# checked `x not in dct` instead of the key; stored the word as a string (no .append on str);
# dct() instead of dct.values().


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dct = {}
        result = []

        for x in strs:
            key = "".join(sorted(x))
            if key not in dct:
                dct[key] = [x]
            else:
                dct[key].append(x)

        return list(dct.values())


if __name__ == "__main__":
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    print(Solution().groupAnagrams([""]))  # [['']]
    print(Solution().groupAnagrams(["a"]))  # [['a']]
