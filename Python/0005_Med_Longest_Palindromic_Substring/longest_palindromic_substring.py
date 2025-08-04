# https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        resultStr = ""
        maxCount = 0

        for i in range(len(s)):
            leftPointer, rightPointer = i, i
            while leftPointer >= 0 and rightPointer < len(s) and s[leftPointer] == s[rightPointer]:
                if (rightPointer - leftPointer + 1) > maxCount:
                    maxCount = (rightPointer - leftPointer + 1)
                    resultStr = s[leftPointer:rightPointer + 1]
                leftPointer -= 1
                rightPointer += 1

            leftPointer, rightPointer = i, i + 1
            while leftPointer >= 0 and rightPointer < len(s) and s[leftPointer] == s[rightPointer]:
                if (rightPointer - leftPointer + 1) > maxCount:
                    maxCount = (rightPointer - leftPointer + 1)
                    resultStr = s[leftPointer:rightPointer + 1]
                leftPointer -= 1
                rightPointer += 1

        return resultStr