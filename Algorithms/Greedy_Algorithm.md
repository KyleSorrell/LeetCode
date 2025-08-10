Greedy Algorithm

Definition:
An algorithmic approach that makes the locally optimal choice at each step without reconsidering previous decisions, aiming to reach a complete solution quickly.

Key Idea:
Always pick the best immediate option available, trusting that this local choice will lead to a globally optimal solution.

When to Use:

- When subproblems can be solved optimally on their own.
- When making the locally best choice leads to a global optimum.
- When backtracking or revising earlier choices is not necessary.

Steps / Approach:

1. At each step, select the best option available right now (locally optimal).
2. Add or apply that choice to the solution.
3. Repeat until the problem is completely solved or no choices remain.

Example Problems:

- Converting integers to Roman numerals.
- Coin change problems (with appropriate denominations).
- Scheduling tasks by earliest finish time.
- Huffman encoding for data compression.
- Activity selection problems.

Key Advantages:

- Efficient and fast, often O(n) time or better.
- Simple and intuitive to implement.
- No extra overhead like recursion or complex data structures.

Time Complexity:
Usually O(n), where n depends on input size or number of choices.

Space Complexity:
Typically O(1) or minimal extra space, depending on implementation.
