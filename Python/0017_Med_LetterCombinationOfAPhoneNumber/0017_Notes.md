Problem:
Given a string of digits from 2-9, return all possible letter combinations the number could represent based on the telephone keypad mapping. Return the combinations in any order. If the input is empty, return an empty list.

Key Points:

- Digits map to letters like on a phone keypad (2 → "abc", 3 → "def", etc.)
- No mapping for digits 0 or 1 (input restricted to 2-9)
- Need all possible combinations formed by picking one letter per digit
- Return all combinations, order doesn’t matter
- If input is empty, return []

Approach:
Use backtracking (depth-first search) to generate all combinations.

Data Structure:
Use a dictionary to map digits to letters,
digit_to_letters = {
"2": "abc", "3": "def", "4": "ghi",
"5": "jkl", "6": "mno", "7": "pqrs",
"8": "tuv", "9": "wxyz"
}

Backtracking Idea:

- Maintain a current partial combination (path) and the current digit index (index) we are processing.
- For the current digit, try all possible letters.
- Append the letter to path and recursively process the next digit (index + 1).
- When index == len(digits), add the current combination to the result list.
- Backtrack by removing the last letter and try other letters.

Time Complexity:

- Suppose input length = n
- Each digit maps to up to 3 letters
- Total combinations in worst case = O(3^n) (exponential)
- Backtracking generates all combinations systematically

Space Complexity:

- Recursion stack depth = n
- Result list stores O(3^n) strings
- Additional space for current path and dictionary is negligible compared to result
