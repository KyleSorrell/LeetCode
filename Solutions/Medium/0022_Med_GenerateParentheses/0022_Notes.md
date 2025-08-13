Problem:
Given n pairs of parentheses, generate all combinations of well-formed parentheses.

- Each combination must be valid (every opening parenthesis is closed).
- Return all combinations in any order.

Time Complexity Requirement:

- Number of valid sequences = Catalan number C(n) = (2n)! / ((n+1)! n!)
- Brute force generating all sequences = O(2^(2n)) → too slow
- Backtracking generates only valid sequences → O(C(n)) time and space

Key Idea:

- Use backtracking / DFS to build sequences step by step.
- Keep counters: open = number of '(' used, close = number of ')' used.
- Rules to maintain validity:
  - Only add '(' if open < n
  - Only add ')' if close < open
- A sequence is valid only if open == close == n.

Transition Logic (Recursive / Backtracking):

1. Base case: open == close == n → current sequence is complete → add to result.
2. Add '(' if open < n → recurse with open + 1.
3. Add ')' if close < open → recurse with close + 1.
4. Backtrack after each recursion step to try other choices.
