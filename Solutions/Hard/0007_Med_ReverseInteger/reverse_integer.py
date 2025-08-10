# https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        maxInt = 2**31 - 1
        minInt = -2**31

        sign = 1 if x >= 0 else -1
        x = abs(x)

        while x != 0:
            rem = x % 10
            if rev > (maxInt - rem) // 10:
                return 0
            rev = rev * 10 + rem
            x = x // 10

        return sign * rev