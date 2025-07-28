Problem:
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

For example, 2 is written as II in Roman numerals, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Notes:
I started by making a dictionary that maps each Roman numeral character to its integer value. Then I loop through the string using an index so I can also look at the next character. For each character, I compare its value to the value of the next character (if there is one). If the current value is smaller than the next one, that means it’s a subtractive case (like IV or IX), so I subtract it from the result; otherwise, I add it. After going through the whole string, the total in result is the integer value of the Roman numeral.
