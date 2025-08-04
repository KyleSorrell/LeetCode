Problem:
Given an input string s and a pattern p, implement regular expression matching with support for:

. which matches any single character

- which matches zero or more of the preceding element

Matching must cover the entire input string, not just part of it.

Notes:
Time Complexity Requirement: No explicit complexity given, but brute force is exponential → we need Dynamic Programming to reduce it to O(m × n).

Key Idea:
We define a 2D DP table:
Let dp[i][j] mean:
Does s[:i] match p[:j]? - dp[0][0] = True → empty string matches empty pattern - dp[i][0] = False for i > 0 → non-empty string can't match empty pattern - dp[0][j] might be True for patterns like "a*" or "a*b\*" that can reduce to empty.

Transition Logic:

- Case 1: p[j - 1] == s[i - 1] or p[j - 1] == '.'
  These match directly →
  dp[i][j] = dp[i - 1][j - 1]

- Case 2: p[j - 1] == '\*'
  Then two sub-cases:

  1. Zero occurrence of preceding character:
     → dp[i][j] = dp[i][j - 2]

  2. One or more occurrences (only if preceding character matches s[i - 1] or is .):
     → dp[i][j] |= dp[i - 1][j]

Example:
s = "aab"
p = "c*a*b"

Visualizing DP Table Initialization:
' ' c _ a _ b
' ' T F T F T F
a F F F T T F
a F F F F T F
b F F F F F T

- '' vs 'c*' → True because c* can be empty
- 'a' vs 'c*a*' → True because 'a' matches the last a\*
- 'aab' vs 'c*a*b' → True ✅

Final Answer:
Return dp[len(s)][len(p)] — whether full string matches full pattern.
