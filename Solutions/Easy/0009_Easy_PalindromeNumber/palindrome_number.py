# https://leetcode.com/problems/palindrome-number/description/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        reverse = string[::-1]
        if reverse == string:
            return True
        else:
            return False