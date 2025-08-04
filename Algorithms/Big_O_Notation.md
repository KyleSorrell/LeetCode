Big O Notation

What is Big-O Time Complexity?
- Big-O describes how the runtime of an algorithm grows as the input size (n) increases.
- It helps us analyze efficiency by focusing on how time changes, not exact times.
- We ignore constant factors and lower order terms — e.g., O(n/2) or O(n + 5) both simplify to O(n).
- Constants matter only for O(1) — constant time algorithms have runtime independent of input size.

Common Big-O Complexities Explained
1. O(1) — Constant Time
  Runtime doesn’t change with input size.
  Example:
  - Accessing an element by index in an array.
  - Inserting, removing, or looking up a key in a hashmap or hash set.

2. O(n) — Linear Time
  Runtime grows proportionally with input size.
  Example:
  - Summing all elements in an array.
  - Looping through all elements once.
  - Inserting/removing in the middle of an array (worst case, because shifting elements).
  - Searching for an element in an unsorted array (worst case: must check all).

3. O(n²) — Quadratic Time
  Runtime grows proportional to the square of input size.
  Common with nested loops iterating over n elements each.
  Example:
  - Iterating over a 2D grid with two nested loops.
  - Insertion sort (inserting in middle n times).
  - Iterating over all pairs or all triplets in an array (can be O(n^3) for triplets).

4. O(n * m)
  Runtime depends on two different input sizes, n and m.
  Example:
  - Iterating over a matrix with n rows and m columns.

5. O(log n) — Logarithmic Time
  Runtime grows very slowly, increases by 1 for every doubling of input size.
  Example:
  - Binary search on a sorted array.
  - Operations on balanced binary search trees.
  - Push/pop in a heap.

6. O(n log n)
  Combination of linear and logarithmic growth.
  Common in efficient sorting algorithms.
  Example:
  - Merge sort, heapsort, built-in sorting functions in many languages.

7. O(2^n) — Exponential Time
  Runtime doubles with each additional input element.
  Typical for recursive algorithms with two branches at each step.
  Example:
  - Computing Fibonacci numbers recursively (naive).
  - Generating all subsets or combinations.

8. O(c^n) — Exponential Time with base c
  Like 2^n but with other constants like 3^n or 4^n.
  More branches in recursion means higher base.

9. O(√n) — Square Root Time
  Rarely seen but worth knowing.
  Example:
  - Finding factors of a number by checking up to its square root.

10. O(n!) — Factorial Time
  Extremely inefficient, grows faster than exponential.
  Occurs in permutations and some complex problems (e.g., traveling salesman).
  Usually means the solution isn’t optimal or feasible for large n.

Additional Notes
- Nested loops don’t always mean O(n²) if the inner loop doesn’t always run n times (e.g., sliding window, monotonic stack).
- We usually consider worst-case time complexity.
- When multiple terms exist, keep only the term with the largest growth rate (e.g., n + n log n → O(n log n)).
- Logarithms are base 2 unless otherwise stated.
- Big-O is about growth rate, not exact performance.
