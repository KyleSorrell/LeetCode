Backtracking Algorithm

Backtracking is a general algorithmic technique for solving problems incrementally, building candidates to the solutions, and abandoning a candidate (“backtracking”) as soon as it determines that this candidate cannot possibly lead to a valid solution. 
It’s like exploring all possible options in a search tree but pruning paths early to avoid unnecessary work.

When to Use Backtracking:
- The problem involves exploring all or many combinations, permutations, or subsets.
- You need to build solutions step-by-step and undo (“backtrack”) choices to explore alternative paths.
- The problem has constraints that allow pruning of invalid partial solutions early.

Common Characteristics:
- Incremental Construction: Build solutions one piece at a time.
- Choice and Exploration: At each step, try all possible options.
- Backtrack: If a partial solution fails constraints, revert the last choice and try other options.
- Often implemented using recursion.

Often Used In:
- Combinatorial problems (permutations, combinations, subsets).
- Constraint satisfaction problems (e.g., Sudoku, N-Queens).
- String parsing and generation (e.g., generating letter combinations).

When Not to Use It:
- Problems that can be solved greedily or with dynamic programming more efficiently.
- When the search space is too large without effective pruning.

Example: Letter Combinations of a Phone Number
- Map digits to letters.
- Recursively build strings by choosing one letter per digit.
- When the string length equals input digits length, add it to results.
- Backtrack by removing the last chosen letter and trying other letters.

Key Advantages:
- Systematic exploration of all candidate solutions.
- Can handle complex constraints by pruning invalid paths early.
- Simple to implement for many combinatorial problems.

Key Disadvantages:
- Potentially exponential time complexity in worst case.
- Can be slow without pruning or optimizations.
