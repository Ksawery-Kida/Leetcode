# 2114. Maximum Number of Words Found in Sentences — Easy
# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/
# Pattern: array of strings, split + max
# Time: O(total characters) | Space: O(n)
# Problem (summary): each sentence is words separated by single spaces -> return the max word count.
# Key idea: sentence.split() -> list of words ("ala ma kota" -> ["ala", "ma", "kota"]),
# len(...) of that list = word count (len(sentence) would count characters!). Collect, return max.
# Syntax gotchas hit: method = dot + parentheses -> sentence.split() (not sentence(split),
# not sentences.split without ()), functions are called len(x) / max(x), not len.x / max.x;
# don't name the loop variable the same as the list (for sentences in sentences).

class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        result = []
        for sentence in sentences:
            result.append(len(sentence.split()))
        return max(result)


if __name__ == "__main__":
    print(Solution().mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))  # 6
    print(Solution().mostWordsFound(["please wait", "continue to fight", "continue to win"]))  # 3
