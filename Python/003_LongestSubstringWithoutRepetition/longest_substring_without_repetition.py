# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charDict = {}
        maxLen = 0
        startPointer = 0
        for endPointer in range(len(s)):
            if s[endPointer] in charDict:
                startPointer = max(startPointer, charDict[s[endPointer]] + 1)
            charDict[s[endPointer]] = endPointer
            maxLen = max(maxLen, endPointer - startPointer + 1)
        return(maxLen)
'''
This solution finds the length of the longest substring without repeating characters. 
It uses a sliding window approach with two pointers: startPointer marks the start of the current substring, and endPointer moves through each character. 
As it goes, it keeps track of the last seen index of each character in a dictionary. 
If it sees a repeating character, it shifts the start pointer to the right of the last time that character appeared. 
It updates the max length of the substring as it moves forward.
'''
