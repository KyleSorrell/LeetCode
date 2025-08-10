Two Pointer Technique

Definition:
A method that uses two pointers (indices) to traverse a data structure like an array or string from different positions, often to reduce nested loops into a single pass.

Key Idea:
Use two pointers moving toward each other or at different speeds to efficiently find pairs, groups, or windows that satisfy conditions without checking all combinations.

When to Use:

- When the data is sorted or can be treated as sorted.
- Finding pairs or groups meeting a condition (e.g., sum equals target).
- Scanning from both ends or maintaining a sliding window.
- Avoiding extra memory by working in-place.

Steps / Approach:

1. Initialize two pointers at relevant positions (start/end or both start
2. Move pointers based on problem logic:
   - Converging pointers move inward depending on conditions.
   - Same-direction pointers move forward at different speeds or adjust to maintain a window.
3. Check conditions at each step and update pointers accordingly.
4. Continue until pointers meet or the problem’s stopping condition is met.

Example Problems:

- Find two numbers in a sorted array whose sum equals a target.
- Detect cycle in a linked list (fast and slow pointers).
- Remove duplicates from a sorted array.
- Find the longest substring without repeating characters.

Key Advantages:

- Improves efficiency by reducing time complexity from O(n²) to O(n).
- Simple to implement once pattern is recognized.
- Works in-place without extra memory overhead.

Time Complexity:
Typically O(n), where n is the length of the input. This depends on a single pass or linear traversal using the two pointers.

Space Complexity:
O(1) extra space, since it uses pointers and usually modifies or reads the input in-place.
