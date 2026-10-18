# 1108. Defanging an IP Address — Easy
# https://leetcode.com/problems/defanging-an-ip-address/
# Pattern: string, built-in method
# Time: O(n) | Space: O(n)
# Problem (summary): replace every "." in an IPv4 address with "[.]".
# Key idea: text.replace("what", "with_what"). Gotchas hit: replace is a METHOD (address.replace(...),
# not replace(...)), arguments are strings so they need quotes, and strings are immutable —
# replace returns a NEW string, it does not change address, so return the result directly.

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


if __name__ == "__main__":
    print(Solution().defangIPaddr("1.1.1.1"))  # 1[.]1[.]1[.]1
    print(Solution().defangIPaddr("255.100.50.0"))  # 255[.]100[.]50[.]0
