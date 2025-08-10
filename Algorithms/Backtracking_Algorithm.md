Backtracking Algorithm

Definition:
A technique that builds solutions incrementally and abandons a candidate as soon as it determines it cannot lead to a valid solution, effectively pruning the search space.

Key Idea:
Explore all possible options step-by-step, and backtrack (undo) choices when they fail constraints, to systematically find all valid solutions.

When to Use:

- When you need to explore many or all combinations, permutations, or subsets.
- When building solutions step-by-step and undoing choices to explore alternatives.
- When constraints allow early pruning of invalid partial solutions.

Steps / Approach:

1. Start building a solution incrementally.
2. At each step, try all possible choices.
3. If a partial solution violates constraints, backtrack by undoing the last choice.
4. Continue until a complete valid solution is formed or all options are exhausted.

Example Problems:

- Generating letter combinations from phone digits.
- Solving Sudoku puzzles.
- N-Queens problem.
- Generating permutations and subsets.

Key Advantages:

- Systematically explores all candidate solutions.
- Efficient pruning of invalid paths reduces unnecessary work.
- Flexible and easy to implement for many combinatorial problems.

Time Complexity:
Potentially exponential (O(k^n)) in the worst case, depending on the branching factor and depth of recursion.

Space Complexity:
O(n) for recursion stack and temporary data structures used during solution construction.
