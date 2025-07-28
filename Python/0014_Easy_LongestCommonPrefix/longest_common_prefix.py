# https://leetcode.com/problems/longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = ""
        # Loop through character positions (zip stops at shortest string)
        for chars in zip(*strs):
            if len(set(chars)) == 1:
                prefix += chars[0]
            else:
                break
        return prefix