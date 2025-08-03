# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if needle in haystack:
            for i in range(0,len(haystack) - len(needle) +1):
                if haystack[i:i+len(needle)] == needle:
                    return i
                
        return -1