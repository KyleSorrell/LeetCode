# https://leetcode.com/problems/zigzag-conversion/description/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        result = []
        cycle_len = 2 * (numRows - 1)

        for row in range(numRows):
            for i in range(row, len(s), cycle_len):
                result.append(s[i])

                diagonal = i + cycle_len - 2 * row
                if 0 < row < numRows - 1 and diagonal < len(s):
                    result.append(s[diagonal])

        return ''.join(result)